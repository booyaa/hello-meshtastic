from email.mime import message
import time
from mudp import send_nodeinfo, send_text_message, conn, node
import requests

# FIXME: create a config
weather_chimes = [9, 12, 18] # what hours should we announce weather?
dad_joke_chimes = [7, 8, 10, 11, 13, 14, 15, 16, 17] # what hours should we announce dad jokes?
user_agent = "Clock Bot v0.0.0 (https://github.com/booyaa/hello-meshtastic)"

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
                message = "Bong!"
                if current_time.tm_hour in weather_chimes:
                    message += f" {weather_forecast()}"
                if current_time.tm_hour in dad_joke_chimes:
                    message += f" {dad_joke()}"
                send_text_message(message)
                print(message)
                time.sleep(1)  # Prevent multiple prints within the same second
            time.sleep(0.5)  # Check time every half second
    except KeyboardInterrupt:
        print("Clock bot stopping...")

def weather_forecast():
    forecast = "" # in case of problems
    try:
        response = requests.get("https://wttr.in?format=4", headers={"User-Agent": user_agent}) # will use our external IP to geolocate
        if response.status_code == 200:
            forecast = response.text
    except requests.RequestException as e:
        print(f"Error fetching weather info: {e}")
    return forecast

def dad_joke():
    joke = ""  # in case of problems
    try:
        response = requests.get("https://icanhazdadjoke.com/", headers={"User-Agent": user_agent, "Accept": "application/json"})
        if response.status_code == 200:
            joke = response.json().get("joke", "No joke found.")
    except requests.RequestException as e:
        print(f"Error fetching dad joke: {e}")
    return joke

if __name__ == "__main__":
    main()

