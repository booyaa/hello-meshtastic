# pewpew

A poor man's thermal gun

## Scratch

TODO: write up

### Thermal camera

[repo](https://github.com/pimoroni/mlx90640-library)

```sh
# thermal camera
gh repo clone pimoroni/mlx90640-library
echo "dtparam=i2c1_baudrate=1000000" >> /boot/firmware/config.txt

# build deps
sudo apt-get install libi2c-dev
sudo apt-get install libavutil-dev libavcodec-dev libavformat-dev
sudo apt install libsdl2-dev

make clean
make I2C_MODE=RPI

# test - plug HDMI cable
sudo examples/fbuf # displays to console
sudo example/hotspot # same but display temperature in the cross hair

# set up python deps
uv venv
uv pip install pillow
python python/rgb-to-gif.py # run for a few seconds then CTRL-C
ls *.gif # make a note of the file name
```

## SPI 240 square LCD display

[repo](https://github.com/pimoroni/st7789-python/blob/main/examples/gif.py)

```sh
# in another session
gh repo clone pimoroni/st7789-python
uv venv
uv pip install st7789 pillow
python examples/gif.py /path/to/rgb-to-gif-image.gif
```
