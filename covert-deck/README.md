# Covert Deck

A writer deck with covert LoRa capabilities.

## Rationale

None at all just an excuse to mash some component together and experiment by 
combining different styles of decks: cyber, writer, hack. The only core value
is that the device must be portable and battery operated.

## Features

- Distraction free writing device
- Audio based feedback (initially USB audio, but will eventually support 
Bluetooth to keep with the theme of being covert)
- No disruptive notifications from the radio (LoRa) when not used
- Optional BBS software to be installed on another radio to facilitate
  - automatic publishing of micro publications
  - limited messaging with your "team" to discuss edits and gather feedback, 
  or just check in to confirm you haven't been eaten by bears
  - research and summarise topics you wish to write about

## Kit list

### Hardware

- pi zero pinouts: [i2c](https://pinout.xyz/pinout/i2c), [spi](https://pinout.xyz/pinout/spi) and [uart](https://pinout.xyz/pinout/uart)
- epaper display - will need to upgrade to a waveshare 2.13" HAT+ for a faster 
refresh [documentation](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_(B)_Manual)
- keyboard - cardkb from m5stack (will eventually replace with a real keyboard
like the gherkin 30%) [pinout](https://github.com/AbeNaws/cardkb-updated?tab=readme-ov-file#connect-cardkb-to-raspberry-pi)
- rotary encoder ([docs](https://github.com/pimoroni/ioe-python/tree/main)) or touchpad ([docs](https://github.com/pimoroni/trackball-python/tree/master)) to navigate quickly on screen

### Software

- eSpeak NG `sudo apt install espeakng`
  - Python module `pip install espeakng`

## Set up notes

### set up i2c

```sh
sudo raspi-config nonint do_i2c 0 # enables i2c
sudo apt-get install i2c-tools # for i2cdetect
i2cdetect -y 1 # verifies devices
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- 0a -- -- -- -- 0f
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --

# 0f = rotary encoder
# 0a = trackball
```

> [!TIP]
> If i2cdetect fails to detect anything or runs really slowly you've probably
got the device plugged in the wrong way around

### setup rotary encoder
```sh
sudo apt-get install python3-dev python3-rpi.gpio # not sure if rpi.gpio is needed
uv venv # set up environment
uv pip install pimoroni-ioexpander RPi.GPIO 
curl -LO https://raw.githubusercontent.com/pimoroni/ioe-python/refs/heads/main/examples/rotary.py
python rotary.py # verify
```

### setup trackball

```sh
uv pip install trackball evdev
gh repo clone pimoroni/trackball-python
cd trackball-python/examples
# not sure how much of the following is needed for a standalone controller vs OS pointer control
sudo modprobe uinput
sudo cp 10-trackball.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
python read-all.py # to learn all events
python colour-control.py # to cycle through colours whilst using trackball
```

### setup cardkb

```sh
uv pip install smbus python-uinput
gh repo clone ian-antking/cardkb
cd cardkb
i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 5f
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
sudo modprobe uinput
lsmod | grep uinput
# uinput                 20480  0
sudo ../.venv/bin/python cardkb &
cat /dev/input/event2
# press some keys
udevadm info /dev/input/event2 # how did we know it was event2?
P: /devices/virtual/input/input2/event2
M: event2
R: 2
J: c13:66
U: input
D: c 13:66
N: input/event2
L: 0
E: DEVPATH=/devices/virtual/input/input2/event2
E: DEVNAME=/dev/input/event2
E: MAJOR=13
E: MINOR=66
E: SUBSYSTEM=input
E: USEC_INITIALIZED=594458903
E: ID_INPUT=1
E: ID_INPUT_KEY=1
E: ID_INPUT_KEYBOARD=1
E: ID_SERIAL=noserial
E: TAGS=:power-switch:
E: CURRENT_TAGS=:power-switch:
```

> [!TIP]
> You may need to jiggle the grove connector until the activity light on the 
keyboard lights up on key press and the device shows up on i2cdetect.

> [!WARNING]
> We won't be able to see any keystokes via SSH, so you need HDMI or serial to 
verify properly
