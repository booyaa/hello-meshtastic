# Resources

## Examples

- [Clock Bot](./clock_bot.py) - Uses mudp to send messages via UDP (requires at least one node on your same network with TCP/IP enabled)
- [Get my Node info](./get_my_node_info.py) - ronseal
- [Meshtastic local API report](./meshtastic_local_json_report.sh). See [HTTP API](https://meshtastic.org/docs/development/device/http-api/) doc and [firmware](https://github.com/meshtastic/firmware/blob/86af5f5252f408fce0fc1509e2430c98395c7d49/src/mesh/http/ContentHandler.cpp#L595) for more details.
- [Send text over Serial](./send_text_serial.py)
- [Send text over Serial with TCP fallback](./send_text_serial_with_tcp_fallback.py) - fairly robust way of trying serial and using tcp fallback. It will also handle when the serial isn't a meshtastic node.
- [Trace Route Bot](./traceroute_bot.py) - sends trace routes if DM
  - un*x `TRACEBOT_COORDS="lat,lon"          PYTHONIOENCODING="utf-8" P     YTHONUTF8=1   python traceroute_bot.py`
  - ps1 `$env:TRACEBOT_COORDS="lat,lon";$env:PYTHONIOENCODING="utf-8"; $env:PYTHONUTF8=1; python .\traceroute_bot.py`

> [!TIP]
> To set environment variable in PowerShell use `$env:TCP_HOSTNAME="1.2.3.4"`. For linux-ish use `export TCP_HOSTNAME="1.2.3.4"`.

### Work in progress

> [!WARNING]
> These scripts maybe non-functional

- [Waiting for ACK](./wip_waiting_for_ack.py) - getting an ack from messages using the sendtext method

### Side Quests

#### ClockBot feature testing in REPL

```sh
python
>>> import clock_bot
>>> clock_bot.weather_forecast()
```

#### News

- [local news headline parser](./wip_local_news.py)
- [rss-parser](https://dhvcc.github.io/rss-parser/)
- [bbc local news rss](https://feeds.bbci.co.uk/news/england/norfolk/rss.xml)

```py
>>> first_item = parse_news.rss.channel.items[0]
>>> print(f"BONG! Local news: {first_item.title.content} {first_item.guid.content}")
BONG! Local news: Dance venue 'won't become car park' as offers made https://www.bbc.com/news/articles/cj0y7jp5nrgo#0
>>> print(len(f"BONG! Local news: {first_item.title.content} {first_item.guid.content}"))
117

>>> len([item.title.content for item in parse_news.rss.channel.items])
22

>>> " ".join([item.title.content for item in parse_news.rss.channel.items])
"Dance venue 'won't become car park' as offers made Woman seriously injured in hit-and-run collision Swimmer, 23, who died had 'the biggest heart' Twins killed in holiday crash 'had special bond' 'Wonderful' ferry resumes crossings after repairs Hemp is star attraction at girls' football event Opening of £47m bypass hailed as 'historic day' Crews tackle forest fire close to A-road Motorcyclist in 50s dies following collision Library locks its doors when open due to anti-social incidents Social clubs warn locals to 'use it or lose it' Chinook crash victim 'would want answers', says sister Hemp grateful for 'special' Carrow Road moment Forson to miss Watford cup tie with hamstring injury Norwich squad still 'building relationships' - Wright Norwich have 'huge amount to do' - Manning The East Anglian rivalry from behind the mic Goreham celebrates 25 years of Canaries commentary ‘Transformational’ bypass now open What’s new at Norwich Castle? Farmwatch How will sale of Norwich Airport affect Norfolk?"
>>> len(" ".join([item.title.content for item in parse_news.rss.channel.items]))
1010
```

#### Train times

See also #trains

```sh
curl -LO https://trntxt.uk/norwich/londonliverpoolstreet # reduced html no JS (I think)
curl -L --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/cargo-bins/cargo-binstall/main/install-from-binstall-release.sh | bash # cargobinstall
export PATH=$HOME/.cargo/bin
cargo-binstall htmlq
cat londonliverpoolstreet | htmlq 'div' --remove-nodes br
```

### MQTT

reference: [chi-mesh](https://chicagolandmesh.org/guides/mqtt/)

- code: [mqtt-client.py](https://github.com/pdxlocations/Meshtastic-Python-Examples/blob/main/MQTT/mqtt-client.py) - not working

#### Works on my T1000-e

- lora
  - ignore MQTT: off
  - OK to MQTT: on
- MQTT
  - enabled: on
  - MQTT Client proxy: on
  - Connect to MQTT via Proxy: on
  - Encryption Enabled: on
  - Map report enabled: off
  - Root topic: `msh/EU_868/England/Norfolk` # check side by side, it has to be identical on all MQTT clients!
- channel
  - name: # must be the same on all MQTT client!
  - default: key `AQ==`
  - uplink: on
  - downlink: on # otherwise we don't get messages
  - allow position requests: off

### Worked once on Heltec V3

- lora
  - ignore MQTT: off # turning on, stops messages from arriving
  - OK to MQTT: on
- MQTT
  - enabled: on
  - MQTT Client proxy: on
  - Connect to MQTT via Proxy: on
  - Encryption enabled: on
  - JSON enabled: on
  - Map report enabled: off
  - Root topic: `msh/EU_868/England/Norfolk` # check side by side, it has to be identical on all MQTT clients!
- channel
  - name: # must be the same on all MQTT client!
  - default: key `AQ==`
  - uplink: on
  - downlink: on # otherwise we don't get messages
  - allow position requests: off

### Using noproto to debug MQTT

```sh
meshtastic -s --no-proto
```

### Using mosquitto tools

```sh
# JSON end point
mosquitto_sub \
  -h mqtt.meshtastic.org -u meshdev -P large4cats \
  -t 'msh/EU_868/England/Norfolk/2/json/CHANNEL_NAME/#' --id 'gandalf-boo'

# THis doesn't work
mosquitto_pub -h mqtt.meshtastic.org -u meshdev -P large4cats -t 'msh/EU_868/England/Norfolk/2/json/YOUR_CHANNEL' --id 'gandalf-boo' -m '{"channel":x,"from":xxx,"hop_start":x,"hops_away":x,"id":xxx,"payload":{"text":"you know it!"},"sender":"!deadface","timestamp":0,"to":xxx,"type":"text"}'

```

```json
{
  "channel":2,
  "from":1111,
  "hop_start":3,
  "hops_away":0,
  "id":3907767157,
  "payload":{"text":"Boom bip "},
  "rssi":-16,"sender":"!deadface","snr":6,"timestamp":0,"to":4294967295,"type":"text"}
```

## Further Reading

### Official Docs

- [API docs](https://python.meshtastic.org/index.html)
- [pubsub topics](https://python.meshtastic.org/#published-pubsub-topics)

### Code Examples from the internet

- [API examples](https://github.com/meshtastic/python/tree/master/examples)
- [pdxlocations/Mestastic-Python-Examples](https://github.com/pdxlocations/Meshtastic-Python-Examples/tree/main)
- [logging file and console handlers](https://stackoverflow.com/a/46098711)

### Guides

- [mestasticd on wsl](https://meshtastic.org/docs/development/reference/md_wsl/)

### Tools

- [web client](https://client.meshtastic.org/)
