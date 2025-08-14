import contextlib
import json
import os
from platform import node
import pprint
from time import sleep
import time
import meshtastic
import meshtastic.tcp_interface
from meshtastic import portnums_pb2
from pubsub import pub
import logging
from logging import handlers
import contextlib

interface = None

# create a basic logging config for console
logging.basicConfig(
    level='INFO',
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
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
    # TODO: refactor and store globally
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
    # portnums_pb2.TELEMETRY_APP is 67 (how we can convert decoded.portnum back to portnums_pb2?)
    if packet_type == "TELEMETRY_APP":
        pass
    else:
        print("=========================================================")
        pprint.pprint(packet)  # Debugging: print the entire packet


# events
pub.subscribe(on_connection, "meshtastic.connection.established")
pub.subscribe(on_receive, "meshtastic.receive")

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
