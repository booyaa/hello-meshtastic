# Covert Deck

A writer deck with covert LoRa capabilities.

## Rationale

None at all just an excuse to mash some component together and experiment by 
combining different styles of decks: cyber, writer, hack. The only core value
is that the device must be portable and battery operated.

## Features

- Distraction free writing device, terminal based
- No disruptive notifications from the radio (LoRa) when not used
- Optional BBS software to be installed on aother radio to facilitate
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
like the gherkin 30%)
- rotary encoder ([docs](https://github.com/pimoroni/ioe-python/tree/main)) or touchpad ([docs](https://github.com/pimoroni/trackball-python/tree/master)) to navigate quickly on screen

### Software

- TBC

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
