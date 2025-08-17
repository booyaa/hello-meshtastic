import os
# from platform import node
from time import sleep
import meshtastic
import meshtastic.tcp_interface
from pubsub import pub
import logging
from logging import handlers

interface = None

logging.basicConfig(
    # Usage: ROVER_BOT_LOG_LEVEL=debug python rover.py
    level=os.getenv('ROVER_BOT_LOG_LEVEL', 'INFO').upper(),
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.handlers.TimedRotatingFileHandler(
            "rover.log", when="midnight", interval=1, backupCount=7
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

def on_receive(packet, topic=pub.AUTO_TOPIC):
    packet_type = packet.get('decoded', {}).get('portnum')

    if packet_type == "TEXT_MESSAGE_APP":
        message = packet.get('decoded', {}).get('payload', '')
        from_node = packet.get('from', 'Unknown')
        to = packet.get('to', 'Unknown') if packet.get('to') != meshtastic.BROADCAST_NUM else 'broadcast'
        from_node_details = get_node_info(from_node)

        if not message.decode().lower().startswith('rover'):
            return  # Ignore non-traceroute messages

        message = message.decode().lower().replace("traceroute", "").strip()
        logging.info(f"{from_node_details['string']} drove rover: {message}")
        interface.sendText(message, channelIndex=0)
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
    return {
        'longName': user_info.get('longName', 'Unknown'),
        'shortName': user_info.get('shortName', 'Unknown'),
        'id': user_info.get('id', 'Unknown'),
        'hwModel': user_info.get('hwModel', 'Unknown'),
        'string': f"{user_info.get('longName', 'Unknown')} ({user_info.get('shortName', 'Unknown')}) ID: {user_info.get('id', 'Unknown')}"
    }

def main():
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
