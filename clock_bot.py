import time
from mudp import send_nodeinfo, send_text_message, conn, node

def setup():
    node.channel = "LongFast"
    node.key = "1PG7OiApB1nwvP+rz05pAQ=="
    node.node_id = "!be11ab07"
    node.long_name = "Mx Clock Bot"
    node.short_name = "⏰"
    MCAST_GRP = "224.0.0.69"
    MCAST_PORT = 4403
    conn.setup_multicast(MCAST_GRP, MCAST_PORT)

def main():
    setup()
    try:
        print("Clock bot started. Sending node info and 'Bong!' every hour...")
        while True:
            current_time = time.localtime()
            if current_time.tm_min == 0 and current_time.tm_sec == 0:
                send_nodeinfo()
                send_text_message("Bong!")
                print("Bong")
                time.sleep(1)  # Prevent multiple prints within the same second
            time.sleep(0.5)  # Check time every half second
    except KeyboardInterrupt:
        print("Clock bot stopping...")

if __name__ == "__main__":
    main()

