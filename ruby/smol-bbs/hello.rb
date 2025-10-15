require 'meshtastic'

puts "Connecting to Meshtastic node..."
@device = Meshtastic.connect(:serial, port: @port)
puts "Connected to Meshtastic node number #{@device.node_num}.\n\n"

@device.on(:packet, lambda { |packet|
  handle_packet(packet)
})

loop do
  sleep 1
end
