#!/bin/bash

tcp_host=$1

if [ -z "$tcp_host" ]; then
  echo "Usage: $0 <tcp_host>"
  exit 1
fi

uvx meshtastic --host "$tcp_host" \
    --set lora.use_preset false \
    --set lora.bandwidth 62 \
    --set lora.spread_factor 8 \
    --set lora.coding_rate 8 \
    --set lora.frequency_offset 0.0 \
    --set lora.channel_num 1 \
    --set lora.override_frequency 869.4313 \
    --ch-index 0 \
    --ch-set name "EdgeFastLow"

echo "Warning: you need to manually fix the channel settings"
