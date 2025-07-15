#!/bin/bash
# Get battery percentage and if the node is charging using meshtastic.local API
curl --silent meshtastic.local/json/report |\
    jq -r '"Battery Percent: \(.data.power.battery_percent)%, Is Charging: \(.data.power.is_charging)"'
