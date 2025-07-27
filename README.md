# Resources

## Examples

- [meshtastic_local_json_report.sh](./meshtastic_local_json_report.sh). See [HTTP API](https://meshtastic.org/docs/development/device/http-api/) doc and [firmware](https://github.com/meshtastic/firmware/blob/86af5f5252f408fce0fc1509e2430c98395c7d49/src/mesh/http/ContentHandler.cpp#L595) for more details.
- [send_text_serial.py](./send_text_serial.py)
- [send_text_serial_with_tcp_fallback.py](./send_text_serial_with_tcp_fallback.py) - fairly robust way of trying serial and using tcp fallback. It will also handle when the serial isn't a meshtastic node.

> [!TIP]
> To set environment variable in PowerShell use `$env:TCP_HOSTNAME="1.2.3.4"`. For linux-ish use `export TCP_HOSTNAME="1.2.3.4"`.

### Work in progress

> [!WARNING]
> These scripts maybe non-functional

- [wip_waiting_for_ack.py](./wip_waiting_for_ack.py) - getting an ack from messages using the sendtext method

## Further Reading

### Official Docs

- [API docs](https://python.meshtastic.org/index.html)
- [pubsub topics](https://python.meshtastic.org/#published-pubsub-topics)

### Examples

- [API examples](https://github.com/meshtastic/python/tree/master/examples)
- [pdxlocations/Mestastic-Python-Examples](https://github.com/pdxlocations/Meshtastic-Python-Examples/tree/main)
- [logging file and console handlers](https://stackoverflow.com/a/46098711)

### Guides

- [mestasticd on wsl](https://meshtastic.org/docs/development/reference/md_wsl/)

### Tools

- [web client](https://client.meshtastic.org/)

