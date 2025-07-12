import meshtastic
import meshtastic.serial_interface
from pubsub import pub
import time

def onConnection(interface, topic=pub.AUTO_TOPIC):
    print("Connected to Meshtastic node. Sending message to public channel...")
    interface.sendText("hello mesh")

pub.subscribe(onConnection, "meshtastic.connection.established")
interface = meshtastic.serial_interface.SerialInterface()

time.sleep(300) # seconds

print("Exiting...")
interface.close()
