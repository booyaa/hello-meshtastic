# Packets

## Useful information

- Node number 4294967295 (the uint32 max value used to indicate a message is a channel message and not a DM) ([source](https://github.com/meshtastic/firmware/issues/5587))

## TEXT_MESSAGE_APP

```python
{'channel': 1,
 'decoded': {'bitfield': 1,
             'payload': b'Boop',
             'portnum': 'TEXT_MESSAGE_APP',
             'text': 'Boop'},
 'from': MY_NODE_NUMBER,
 'fromId': '!feedface',
 'hopLimit': 3,
 'hopStart': 3,
 'id': 2102132719,
 'raw': from: MY_NODE_NUMBER
to: 4294967295
channel: 1
decoded {
  portnum: TEXT_MESSAGE_APP
  payload: "Boop"
  bitfield: 1
}
id: 2102132719
rx_time: 1755164565
rx_snr: 6.25
hop_limit: 3
rx_rssi: -29
hop_start: 3
relay_node: 34
,
 'relayNode': 34,
 'rxRssi': -29,
 'rxSnr': 6.25,
 'rxTime': 1755164565,
 'to': 4294967295,
 'toId': '^all'}
```

## NODEINFO_APP

```python
{'decoded': {'bitfield': 3,
             'payload': b'possibly node info string?',
             'portnum': 'NODEINFO_APP',
             'user': {'hwModel': 'MY_RADIO_HW',
                      'id': '!feedface',
                      'isUnmessagable': False,
                      'longName': 'MY_NODE_LONG_NAME',
                      'macaddr': 'xxx',
                      'publicKey': 'redacted=',
                      'raw': id: "!feedface"
long_name: "MY_NODE_LONG_NAME"
short_name: "🧭"
macaddr: "redacted"
hw_model: MY_RADIO_HW
role: CLIENT_MUTE
public_key: "redacted"
is_unmessagable: false
,
                      'role': 'CLIENT_MUTE',
                      'shortName': '🧭'},
             'wantResponse': True},
 'from': MY_NODE_NUMBER,
 'fromId': '!feedface',
 'hopLimit': 3,
 'hopStart': 3,
 'id': 3772554509,
 'raw': from: MY_NODE_NUMBER
to: 4294967295
decoded {
  portnum: NODEINFO_APP
  payload: "possibly node info string?"
  want_response: true
  bitfield: 3
}
id: 3772554509
rx_time: 1755164649
rx_snr: 5.75
hop_limit: 3
rx_rssi: -22
hop_start: 3
relay_node: 34
,
 'relayNode': 34,
 'rxRssi': -22,
 'rxSnr': 5.75,
 'rxTime': 1755164649,
 'to': 4294967295,
 'toId': '^all'}
```

## TRACEROUTE_APP

```python
{'decoded': {'bitfield': 3,
             'payload': b'redacted',
             'portnum': 'TRACEROUTE_APP',
             'traceroute': {'raw': snr_towards: 25
, 'snrTowards': [25]},
             'wantResponse': True},
 'from': MY_NODE_NUMBER,
 'fromId': '!feedface',
 'hopLimit': 3,
 'hopStart': 3,
 'id': 3260809683,
 'nextHop': 184,
 'raw': from: MY_NODE_NUMBER
to: DEST_NODE_NUM
decoded {
  portnum: TRACEROUTE_APP
  payload: "redacted"
  want_response: true
  bitfield: 3
}
id: 3260809683
rx_time: 1755164754
rx_snr: 6.25
hop_limit: 3
want_ack: true
rx_rssi: -32
hop_start: 3
next_hop: 184
relay_node: 34
,
 'relayNode': 34,
 'rxRssi': -32,
 'rxSnr': 6.25,
 'rxTime': 1755164754,
 'to': DEST_NODE_NUM,
 'toId': '!deadbeef',
 'wantAck': True}
```

## ROUTING_APP

```python
{'decoded': {'bitfield': 1,
             'payload': b'redacted',
             'portnum': 'ROUTING_APP',
             'requestId': 2437680628,
             'routing': {'errorReason': 'NONE', 'raw': error_reason: NONE
}},
 'from': MY_NODE_NUMBER,
 'fromId': '!feedface',
 'id': 1867130130,
 'raw': from: MY_NODE_NUMBER
to: DEST_NODE_NUM
decoded {
  portnum: ROUTING_APP
  payload: "redacted"
  request_id: 2437680628
  bitfield: 1
}
id: 1867130130
rx_time: 1755164756
rx_snr: 6.5
rx_rssi: -35
,
 'rxRssi': -35,
 'rxSnr': 6.5,
 'rxTime': 1755164756,
 'to': DEST_NODE_NUM,
 'toId': '!deadbeef'}
```

## TELEMETRY_APP

```python
{'decoded': {'bitfield': 1,
             'payload': b'redacted',
             'portnum': 'TELEMETRY_APP',
             'telemetry': {'deviceMetrics': {'airUtilTx': 0.14472222,
                                             'batteryLevel': 101,
                                             'channelUtilization': 0.0,
                                             'uptimeSeconds': 15190,
                                             'voltage': 4.18},
                           'raw': time: 1755164980
device_metrics {
  battery_level: 101
  voltage: 4.18
  channel_utilization: 0
  air_util_tx: 0.144722223
  uptime_seconds: 15190
}
,
                           'time': 1755164980}},
 'from': MY_NODE_NUMBER,
 'fromId': '!feedface',
 'hopLimit': 3,
 'hopStart': 3,
 'id': 3132070171,
 'raw': from: MY_NODE_NUMBER
to: 4294967295
decoded {
  portnum: TELEMETRY_APP
  payload: "redacted"
  bitfield: 1
}
id: 3132070171
rx_time: 1755164980
rx_snr: 6.75
hop_limit: 3
rx_rssi: -30
hop_start: 3
relay_node: 34
,
 'relayNode': 34,
 'rxRssi': -30,
 'rxSnr': 6.75,
 'rxTime': 1755164980,
 'to': 4294967295,
 'toId': '^all'}
```

## POSITION_APP

```python
{'decoded': {'bitfield': 1,
             'payload': b'redacted',
             'portnum': 'POSITION_APP',
             'position': {'altitude': 0,
                          'groundSpeed': 0,
                          'groundTrack': 0,
                          'latitude': 0.0,
                          'latitudeI': 0,
                          'locationSource': 'LOC_MANUAL',
                          'longitude': 0.0,
                          'longitudeI': 0,
                          'precisionBits': 13,
                          'raw': latitude_i: 0
longitude_i: 0
altitude: 0
location_source: LOC_MANUAL
ground_speed: 0
ground_track: 0
precision_bits: 13
}},
 'from': ANOTHER_NODE_NUM,
 'fromId': '!c0ffeeed',
 'hopLimit': 3,
 'hopStart': 3,
 'id': 335737339,
 'priority': 'BACKGROUND',
 'raw': from: ANOTHER_NODE_NUM
to: 4294967295
decoded {
  portnum: POSITION_APP
  payload: "redacted"
  bitfield: 1
}
id: 335737339
rx_time: 1755165463
hop_limit: 3
priority: BACKGROUND
hop_start: 3
relay_node: 184
,
 'relayNode': 184,
 'rxTime': 1755165463,
 'to': 4294967295,
 'toId': '^all'}
```

## UDP NODEINFO_APP

```python
{'decoded': {'bitfield': 1,
             'payload': b'\n\t!be11ab07\x12\x0cMx Clock Bot\x1a\x03\xe2'
                        b'\x8f\xb0(\xff\x01',
             'portnum': 'NODEINFO_APP',
             'user': {'hwModel': 'PRIVATE_HW',
                      'id': '!be11ab07',
                      'longName': 'Mx Clock Bot',
                      'raw': id: "!be11ab07"
long_name: "Mx Clock Bot"
short_name: "⏰"
hw_model: PRIVATE_HW
,
                      'shortName': '⏰'}},
 'from': 3188828935,
 'fromId': '!be11ab07',
 'hopLimit': 3,
 'hopStart': 3,
 'id': 777458404,
 'raw': from: 3188828935
to: 4294967295
decoded {
  portnum: NODEINFO_APP
  payload: "\n\t!be11ab07\022\014Mx Clock Bot\032\003\342\217\260(\377\001"
  bitfield: 1
}
id: 777458404
rx_time: 1755165600
hop_limit: 3
hop_start: 3
,
 'rxTime': 1755165600,
 'to': 4294967295,
 'toId': '^all'}
```

## UDP TEXT_MESSAGE_APP

```python
{'decoded': {'bitfield': 1,
             'payload': b'Bong! A police officer caught two kids playing with '
                        b'a firework and a car battery. He charged one and let'
                        b' the other one off.',
             'portnum': 'TEXT_MESSAGE_APP',
             'text': 'Bong! A police officer caught two kids playing with a '
                     'firework and a car battery. He charged one and let the '
                     'other one off.'},
 'from': 3188828935,
 'fromId': '!be11ab07',
 'hopLimit': 3,
 'hopStart': 3,
 'id': 3496711909,
 'raw': from: 3188828935
to: 4294967295
decoded {
  portnum: TEXT_MESSAGE_APP
  payload: "Bong! A police officer caught two kids playing with a firework and a car battery. He charged one and let the other one off."
  bitfield: 1
}
id: 3496711909
rx_time: 1755165600
hop_limit: 3
hop_start: 3
,
 'rxTime': 1755165600,
 'to': 4294967295,
 'toId': '^all'}
```
