import os
import time
import meshtastic
import meshtastic.mesh_interface
import meshtastic.serial_interface
import meshtastic.tcp_interface
from pubsub import pub
from serial import SerialException

def onConnection(interface, topic=pub.AUTO_TOPIC):
    my_node_info = interface.getMyNodeInfo()
    print(f"Connected to Meshtastic node...")
    import pprint
    pprint.pp(my_node_info)

# https://python.meshtastic.org/#published-pubsub-topics
pub.subscribe(onConnection, "meshtastic.connection.established")

interface = None

print("Attempting serial connection to Meshtastic node...")
try:
    interface = meshtastic.serial_interface.SerialInterface()
except meshtastic.mesh_interface.MeshInterface.MeshInterfaceError as e:
    print("Serial connection timed out or failed (preventing tcp fallback). Are you plugged into a Meshtastic device?")

if interface is None or interface.devPath is None:
    print("Trying manual TCP connection fallback...")
    tcp_hostname = os.getenv('MESHTASTIC_HOST', 'meshtastic.local')
    try:
        interface = meshtastic.tcp_interface.TCPInterface(hostname=tcp_hostname)
        print("Sleeping for 5 seconds......")
        time.sleep(5)  # Allow some time for the connection to establish
    except Exception as e:
        print("Failed to connect to Meshtastic node using meshtastic.local.")
        print("Please set the MESHTASTIC_HOST environment variable to your Meshtastic node's IP address.")
        exit(1)
    finally:
        interface.close()
