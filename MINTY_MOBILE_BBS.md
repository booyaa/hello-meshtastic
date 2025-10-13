# Minty Mobile BBS

## Kit list

- Raspberry Pi Zero 2WH
- Waveshare UPS C hat w/ 1000 mAh battery
- Waveshare 2.13 e-Paper Display
- Seeed studio XIAO S3-32 Wio SX-1262

## Pi config

- Bookworm 64-bit
- ~~One CPU core active~~ reverted because a lot of stuff needs multi cores (see warning)

```diff
#/boot/firmware/cmdline.txt
-console=serial0,115200 console=tty1 root=PARTUUID=e8c1cddb-02 rootfstype=ext4 fsck.repair=yes rootwait cfg80211.ieee80211_regdom=GB
+console=serial0,115200 console=tty1 maxcpus=1 root=PARTUUID=e8c1cddb-02 rootfstype=ext4 fsck.repair=yes rootwait cfg80211.ieee80211_regdom=GB
```

> [!WARNING]
> One CPU core may cause problems with multi threaded software. Example MeshBBS need at least two cores because the serial connnection is thread for reads and writes.

- HDMI off

```diff
#
-dtoverlay=vc4-kms-v3d
+dtoverlay=vc4-kms-v3d,nohdmi
```

## BBS software

A [fork](https://github.com/booyaa/Hops) of [Hops](https://github.com/morria/Hops).

## UPS-C Hat

- requires `smbc` pip
- Accurancy of INA219's current load may be suspect. It's 800 mAh irrespective of number of CPUs online (source: [Jeff Geerling](https://www.jeffgeerling.com/blog/2021/disabling-cores-reduce-pi-zero-2-ws-power-consumption-half)). The radio according to the chip draws an additional 500 mAh.

## e-Paper Display Hat

Will add the code here when it's ready. In the meanwhile please see these
[instructions](https://github.com/booyaa/hello-waveshare-epaper-display/blob/main/README.md#verifying-device-works) for verifying your hat works.

## Wio SX-1262

Using the [radio](https://wiki.seeedstudio.com/wio_sx1262/) that comes with the
Seeed XIAO starter kit and the [lora-MeshAdv-Mini-900M22S.yaml](https://github.com/meshtastic/firmware/blob/develop/bin/config.d/lora-MeshAdv-Mini-900M22S.yaml) config.

### Config and pin mapping

| radio          | pi gpio |
| :------------- | :---------------- |
| CS (NSS)     6 | 8                 |
| IRQ (DIO1)  12 | 16                |
| Busy        11 | 20                |
| Reset        5 | 24                |
| RXen (MOSI)  3 | 12                |

---------------------------------------
| Power.       8 | 1 (3.3v) 2 (5v).  |
| Ground       7 | 6                 |

DIO2_AS_RF_SWITCH: true
DIO3_TCXO_VOLTAGE: true

###  WIO SX-1262 Pinout

| left      | right     |
| :-------- | :-------- |
| 1 - DIO1  | 2 - Vin   |
| 3 - BUSY  | 4 - Gnd   |
| 5 - RST   | 6 - 3v3   |
| 7 - NSS   | 8 - MOSI  |
| 9 - RF-SW | 10 - MISO |
| 11 - D5   | 12 - SCK  |
| 13 - D6   | 14 - D7   |

### Raspberry Pi Pinout

| left          | right                   |
| :------------ | :---------------------- |
| 1 - 3v3 Power | 2 - 5v power            |
| 3 - N/A       | 4 - 5v power            |
| 5 - N/A       | 6 - Groumd              |
| 7 - N/A       | 8 - GPIO 14 (UART TX)   |
| 9 - N/A       | 10 - N/A                |
| 11 - N/A      | 12 - GPIO 18 (SPI1 CE0) |
| 13 - N/A      | 14 - N/A                |
| 15 - N/A      | 16 - GPIO23             |
| 17 - N/A      | 18 - N/A                |
| 19 - N/A      | 20 - Ground             |
| 21 - N/A      | 22 - N/A                |
| 23 - N/A      | 24 - GPIO 8 (SPIO CE0)  |
