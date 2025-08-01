# Resources

## Examples

- [Clock Bot](./clock_bot.py) - Uses mudp to send messages via UDP (requires at least one node on your same network with TCP/IP enabled)
- [Get my Node info](./get_my_node_info.py) - ronseal
- [Meshtastic local API report](./meshtastic_local_json_report.sh). See [HTTP API](https://meshtastic.org/docs/development/device/http-api/) doc and [firmware](https://github.com/meshtastic/firmware/blob/86af5f5252f408fce0fc1509e2430c98395c7d49/src/mesh/http/ContentHandler.cpp#L595) for more details.
- [Send text over Serial](./send_text_serial.py)
- [Send text over Serial with TCP fallback](./send_text_serial_with_tcp_fallback.py) - fairly robust way of trying serial and using tcp fallback. It will also handle when the serial isn't a meshtastic node.
- [Trace Route Bot](./traceroute_bot.py) - sends trace routes if DM
    - `$env:PYTHONIOENCODING="utf-8"; $env:PYTHONUTF8=1; python .\traceroute_bot.py`

> [!TIP]
> To set environment variable in PowerShell use `$env:TCP_HOSTNAME="1.2.3.4"`. For linux-ish use `export TCP_HOSTNAME="1.2.3.4"`.

### Work in progress

> [!WARNING]
> These scripts maybe non-functional

- [Waiting for ACK](./wip_waiting_for_ack.py) - getting an ack from messages using the sendtext method

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
