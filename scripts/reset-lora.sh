#!/bin/bash

tcp_host=$1

if [ -z "$tcp_host" ]; then
  echo "Usage: $0 <tcp_host>"
  exit 1
fi

uvx meshtastic --host "$tcp_host" \
    --set lora.modem_preset LONG_FAST \
    --set lora.bandwidth 0 \
    --set lora.spread_factor 0 \
    --set lora.coding_rate 0 \
    --set lora.frequency_offset 0.0

echo "Warning: you need to manually fix the channel settings"
