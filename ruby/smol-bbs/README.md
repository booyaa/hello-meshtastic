# Smol BBS

A smol BBS written hopefully in Ruby

## Notes

```sh
# skip asdf if you don't want to build ruby from scratch
asdf set ruby 3.4.1 # or whatever else is available in 3.4.x
asdf plugin add ruby
asdf install ruby 3.4.7

# use docker instead
docker build -t smol-bbs .
docker run --device=/dev/ttyUSB0 smol-bbs

# bootstrapping
bundle init
bundle add meshtastic-client --github "blaknite/meshtastic-client"
```
