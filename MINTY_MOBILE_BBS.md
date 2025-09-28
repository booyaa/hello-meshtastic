# Minty Mobile BBS

## Kit list

- Raspberry Pi Zero 2WH
- Waveshare UPS C hat
- Seeed studio XIAO S3-32 Wio SX-1262

## Pi config

- Bookworm 64-bit
- One CPU core active

```diff
#/boot/firmware/cmdline.txt
-console=serial0,115200 console=tty1 root=PARTUUID=e8c1cddb-02 rootfstype=ext4 fsck.repair=yes rootwait cfg80211.ieee80211_regdom=GB
+console=serial0,115200 console=tty1 maxcpus=1 root=PARTUUID=e8c1cddb-02 rootfstype=ext4 fsck.repair=yes rootwait cfg80211.ieee80211_regdom=GB
```

- HDMI off

```diff
#
-dtoverlay=vc4-kms-v3d
+dtoverlay=vc4-kms-v3d,nohdmi
```

## BBS software

A [fork](https://github.com/booyaa/Hops) of [Hops](https://github.com/morria/Hops).