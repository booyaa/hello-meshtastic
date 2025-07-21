import time
import meshtastic
import meshtastic.tcp_interface
from pubsub import pub

# notes
# usage of the function
# - https://github.com/dudash/python/blob/e2fe359527a88cf649e9f05cd7ad8fc6f0c766aa/meshtastic/__main__.py#L982-L986
#
# some hints from mian on discord (thanks btw)
#
# On the interface.sendText call, add an argument onResponse=interface.localNode.onAckNak
# - sendtext - https://python.meshtastic.org/mesh_interface.html#meshtastic.mesh_interface.MeshInterface.sendText
#
# You may still get timeouts, of course, and for a broadcast message such as this you will only get an implicit acknowledgement. If you're curious what's being done there, look at the onAckNak function in meshtastic/node.py
# - onAckNak - https://python.meshtastic.org/node.html#meshtastic.node.Node.onAckNak
#
# (and the waitForAckNak method in meshtastic/mesh_interface.py) in the library repo; you might be able to do something more manually that serves your specific needs better, depending.
# - waitForAckNak - https://python.meshtastic.org/mesh_interface.html#meshtastic.mesh_interface.MeshInterface.waitForAckNak
#
# also run sendtext in debug mode to see what's going on:
# meshtastic --debug --sendtext "hello mesh" --channel 1 --destination '!shortname' --ack

def on_receive(packet, interface):  # pylint: disable=unused-argument
    """called when a packet arrives"""
    packet_type = packet.get('decoded', {}).get('portnum', 'unknown')
    if packet_type == 'TELEMETRY_APP':
        return # Ignore telemetry packets

    print(f"Received: {packet}")


def on_connection(interface, topic=pub.AUTO_TOPIC):  # pylint: disable=unused-argument
    """called when we (re)connect to the radio"""
    print("sending text message...")
    # interface.sendText("hello mesh", channelIndex=1, onResponse=interface.localNode.onAckNak)
    interface.sendText("hello mesh", destinationId='!a0cb1e98', onResponse=interface.localNode.onAckNak)

    # print("waiting for acknowledgements...")
    # interface.waitForAckNak()

    print("acknowledgements received.")

interface = meshtastic.tcp_interface.TCPInterface(hostname='192.168.1.90')
pub.subscribe(on_connection, "meshtastic.connection.established")
pub.subscribe(on_receive, "meshtastic.receive")

print(interface.localNode)

print("🔌 Connecting to Meshtastic node...")

print("🕒 Waiting for event... Press Ctrl+C to stop.")
try:
    while True:
        time.sleep(1000)
except KeyboardInterrupt:
    print("🛑 Exiting.")
finally:
    interface.close()

