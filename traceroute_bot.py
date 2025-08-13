import contextlib
import os
from platform import node
import pprint
from time import sleep
import time
import meshtastic
import meshtastic.tcp_interface
from pubsub import pub
import logging
from logging import handlers
import contextlib
import io
import math

interface = None
# initialise last run 30 seconds ago to avoid rate limiting on start up
last_run = time.localtime(time.time() - 30)
our_coords = None  # (latitude, longitude)

logging.basicConfig(
    # Usage: TRACEROUTE_BOT_LOG_LEVEL=debug python traceroute_bot.py
    level=os.getenv('TRACEROUTE_BOT_LOG_LEVEL', 'INFO').upper(),
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.handlers.TimedRotatingFileHandler(
            "traceroute_bot.log", when="midnight", interval=1, backupCount=7
        )  # Daily log rotation at midnight, keep 7 days of logs
    ]
)

# event handlers
def on_connection(interface, topic=pub.AUTO_TOPIC):
    global my_node_info
    my_node_info = interface.getMyNodeInfo()
    battery_level = my_node_info.get('deviceMetrics',{}).get('batteryLevel', 'unknown')
    long_name = my_node_info.get('user', {}).get('longName', 'Unknown')
    id = my_node_info.get('user', {}).get('id', 'Unknown')
    logging.info(f"Connected to {long_name} (ID: {id}), Battery Level: {battery_level}%")

    node = interface.getNode('^local')
    global our_coords
    if our_coords is None:
        node_info = interface.getMyNodeInfo()
        our_coords = (node_info.get('position', {}).get('latitude', {}), node_info.get('position', {}).get('longitude', {}))
        logging.warning(f"No coordinates set using TRACEBOT_COORDS, using default from device: {our_coords}")
    channels = node.channels
    channel_log = ""
    if channels:
        channel_log = "Listening on channels:"
        for channel in channels:
            if channel.role:
                channel_log += f" {"default" if len(channel.settings.name) == 0 else channel.settings.name} (ch: {channel.index}) - {"primary" if channel.role == 1 else "secondary"} /"
        channel_log = channel_log[:-2] # trim trailing separator
    else:
        channel_log = "No channels found."

    logging.info(channel_log)


def on_receive(packet, topic=pub.AUTO_TOPIC):
    packet_type = packet.get('decoded', {}).get('portnum')

    if packet_type == "TEXT_MESSAGE_APP":
        message = packet.get('decoded', {}).get('payload', '')
        from_node = packet.get('from', 'Unknown')
        to = packet.get('to', 'Unknown') if packet.get('to') != meshtastic.BROADCAST_NUM else 'broadcast'
        from_node_details = get_node_info(from_node)

        # andor injoke for status check
        if message.decode().lower().startswith ('on program'):
            channel = packet.get('channel',0)
            interface.sendText("(puts hands on head)", channelIndex=channel)
            return  # we're done 
           
        # last guard rail before we being trace routing
        # FIXME: this could be better branched
        if not message.decode().lower().startswith('traceroute'):
            return  # Ignore non-traceroute messages
        
        message = message.decode().lower().replace("traceroute", "").strip()
        parts = message.split(",")
        if len(parts) == 3:
            latitude = float(parts[0].strip())
            longitude = float(parts[1].strip())
            label = parts[2].strip() + " - "or ""
        else:
            latitude = longitude = None
            label = message + " - " if len(message) > 0 else ""
            print("DEBUG", label)
        
        # add cool off period
        current_time = time.localtime()
        elapsed_seconds = (current_time.tm_min * 60 + current_time.tm_sec) - (last_run.tm_min * 60 + last_run.tm_sec)
        logging.info(f"Elapsed seconds since last traceroute: {elapsed_seconds}")
        if elapsed_seconds <= 30 and elapsed_seconds > 0: # ios
            logging.warning(f"Skipping traceroute due to rate limiting, elapsed seconds: {elapsed_seconds}")
            traceroute = "skipped"
        else:
            traceroute = lazy_traceroute(from_node)
        
        global our_coords
        destination_coords = from_node_details['coords'] if latitude is None or longitude is None else (latitude, longitude)
        if latitude is None or longitude is None:
            logging.warning(f"Using device coordinates: {destination_coords} for distance measuring. This maybe inaccurate unless channel is using precision.")

        print(f"DEBUG|Coords: {destination_coords}, Label: {label}, Elapsed seconds: {elapsed_seconds}")
        distance_to_destination = distance(our_coords, destination_coords)
        logging.info(f"{label}{traceroute} - distance to destination: {distance_to_destination:.2f} km")
    else:
        logging.debug(f"Received packet of type {packet_type}")

# events
pub.subscribe(on_connection, "meshtastic.connection.established")
pub.subscribe(on_receive, "meshtastic.receive")

# helpers
def get_node_info(node_num):
    global interface

    """Retrieve node information by node number."""
    node_info = interface.nodesByNum.get(node_num, {})
    user_info = node_info.get('user', {})
    coords = (node_info.get('position', {}).get('latitude', {}), node_info.get('position', {}).get('longitude', {}))
    return {
        'longName': user_info.get('longName', 'Unknown'),
        'shortName': user_info.get('shortName', 'Unknown'),
        'id': user_info.get('id', 'Unknown'),
        'hwModel': user_info.get('hwModel', 'Unknown'),
        'coords': coords,
        'string': f"{user_info.get('longName', 'Unknown')} ({user_info.get('shortName', 'Unknown')}) ID: {user_info.get('id', 'Unknown')} Hardware: {user_info.get('hwModel', 'Unknown')} Coords: {coords}"
    }

def lazy_traceroute(from_node):
    message = None
    try:
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            interface.sendTraceRoute(dest=from_node, hopLimit=5)
        message = f.getvalue().replace('\n', ' ')
        global last_run
        last_run = time.localtime()
    except interface.MeshInterfaceError as e:
        message = f"Failed to send traceroute: {e}"
        logging.error(message)

    return message

def distance(origin, destination):
    """
    Source: https://stackoverflow.com/a/38187562
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

def main():
    global our_coords
    tracebot_env_coords = os.getenv("TRACEBOT_COORDS", None)
    if tracebot_env_coords:
        try:
            latitude, longitude = map(float, tracebot_env_coords.split(","))
            our_coords = (latitude, longitude)
            logging.info(f"Using coordinates from TRACEBOT_COORDS: {our_coords}")
        except ValueError:
            logging.error(f"Invalid TRACEBOT_COORDS format: {tracebot_env_coords}")

    tcp_hostname = os.getenv('MESHTASTIC_HOST', 'meshtastic.local')
    try:
        global interface
        interface = meshtastic.tcp_interface.TCPInterface(hostname=tcp_hostname)
        while True:
            sleep(1)
            try:
                interface.sendHeartbeat()  # Keep the connection alive
            except interface.MeshInterfaceError as e:
                logging.error(f"Heartbeat failed: {e}")
                # FIXME: try to reconnect
                break
    except KeyboardInterrupt:
        logging.info("Keyboard interrupt received. Exiting...")
    except Exception as e:
        logging.error("Failed to connect to Meshtastic node using meshtastic.local.")
        logging.error("Please set the MESHTASTIC_HOST environment variable to your Meshtastic node's IP address.")
        exit(1) # no interface to close
    finally:
        interface.close()



if __name__ == "__main__":
    logging.info("Starting Meshtastic TCP client...")
    main()
