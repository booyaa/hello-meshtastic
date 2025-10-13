# Minty Mobile BBS

## Kit list

- Raspberry Pi Zero 2WH
- Waveshare UPS C hat w/ 1000 mAh battery
- Waveshare 2.13 e-Paper Display
- Seeed studio XIAO S3-32 Wio SX-1262

## Pi config

- Bookworm 64-bit
- One CPU core active

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
