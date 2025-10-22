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

A [fork][gh_hops_fork] of [Hops][gh_hops].

## UPS-C Hat

- requires `smbc` pip
- Accurancy of INA219's current load may be suspect. It's 800 mAh irrespective of number of CPUs online (source: [Jeff Geerling][geeling_pi_power]). The radio according to the chip draws an additional 500 mAh.

## e-Paper Display Hat

Will add the code here when it's ready. In the meanwhile please see these
[instructions][ws_epd] for verifying your hat works.

## Wio SX-1262

Using the [radio][ws_sx1262_starter_kit]
that comes with the Seeed XIAO starter kit and the config.

### Mestastic config

Now using [lora-lyra-picocalc-wio-sx1262.yaml][gh_meshtasticd_lora_lyra_picocalc] (was using [lora-MeshAdv-Mini-900M22S.yaml][gh_meshtasticd_lora_meshadv_mini]).

```yaml
Lora:
  Module: sx1262
  DIO2_AS_RF_SWITCH: true
  DIO3_TCXO_VOLTAGE: true
  gpiochip: 0
  MOSI: 12
  MISO: 13
  IRQ: 1
  Busy: 23
  Reset: 22
  RXen: 0
  gpiochip: 1
  CS: 9
  SCK: 11
#  TXen: bridge to DIO2 on E22 module
  SX126X_MAX_POWER: 22
  spidev: spidev1.0
  spiSpeed: 2000000
```

### Config and pin mapping

| radio          | pi  | Notes                      |
| :------------- | :-- | :------------------------- |
| IRQ (DIO1)   1 | 1   |                            |
| CS (NSS)     7 | 8   |                            |
| RF-SW (RXen) 9 | 0   | was MOSI (Radio) / 12 (Pi) |
| Reset        5 | 22  | was 24 (Pi)                |
| Busy         3 | 23  | was 20 (Pi)                |
| MOSI         8 | 12  |                            |
| MISO        10 | 13  |                            |
| SCK         12 | 11  |                            |

What about these?

| radio          | pi  | Notes                      |
| :------------- | :-- | :------------------------- |
| Ground       2 | 6   |                            |
| Power        4 | ?   | was 1 (Pi) 3.3v            |

###  WIO SX-1262 Pinout

> [!IMPORTANT]
> The pinout for starter kit is different to the stand alone module

| left       | right      |
| :--------- | :--=------ |
|  1 - DIO1  |  2 - Vin   |
|  3 - BUSY  |  4 - Gnd   |
|  5 - RST   |  6 - 3v3   |
|  7 - NSS   |  8 - MOSI  |
|  9 - RF-SW | 10 - MISO  |
| 11 - D5    | 12 - SCK   |
| 13 - D6    | 14 - D7    |

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


<!-- links -->
[gh_hops_fork]: https://github.com/booyaa/Hops
[gh_hops]: https://github.com/morria/Hops
[geeling_pi_power]: https://www.jeffgeerling.com/blog/2021/disabling-cores-reduce-pi-zero-2-ws-power-consumption-half
[ws_epd]: https://github.com/booyaa/hello-waveshare-epaper-display/blob/main/README.md#verifying-device-works
[ws_sx1262_starter_kit]: https://wiki.seeedstudio.com/wio_sx1262_with_xiao_esp32s3_kit/
[gh_meshtasticd_lora_meshadv_mini]: https://github.com/meshtastic/firmware/blob/develop/bin/config.d/lora-MeshAdv-Mini-900M22S.yaml
[gh_meshtasticd_lora_lyra_picocalc]: https://github.com/meshtastic/firmware/blob/develop/bin/config.d/lora-lyra-picocalc-wio-sx1262.yaml
