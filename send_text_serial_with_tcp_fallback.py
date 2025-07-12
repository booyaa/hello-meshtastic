import os
import time
import meshtastic
import meshtastic.serial_interface
import meshtastic.tcp_interface
from pubsub import pub
from serial import SerialException

def onConnection(interface, topic=pub.AUTO_TOPIC):
    print("Connected to Meshtastic node. Sending message to public channel...")
    interface.sendText("hello mesh!", channelIndex=0)

# https://python.meshtastic.org/#published-pubsub-topics
pub.subscribe(onConnection, "meshtastic.connection.established")

interface = meshtastic.serial_interface.SerialInterface()

if interface.devPath is None:
    print("Trying manual TCP connection fallback...")
    tcp_hostname = os.getenv('MESHTASTIC_HOST', 'meshtastic.local')
    try:
        interface = meshtastic.tcp_interface.TCPInterface(hostname=tcp_hostname)
    except Exception as e:
        print("Failed to connect to Meshtastic node using meshtastic.local.")
        print("Please set the MESHTASTIC_HOST environment variable to your Meshtastic node's IP address.")
        exit(1)

time.sleep(5)  # Allow some time for the connection to establish
print("Exiting...")
# finally:
interface.close()
