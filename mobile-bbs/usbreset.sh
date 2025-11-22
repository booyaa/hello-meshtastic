#!/bin/bash
# source: https://superuser.com/a/1751983/52458
#Devices:
#  Number 001/002  ID 2886:0059  seeed-xiao-s3
#
# FIXME: should be able to get these device IDs from lsusb output or python
lsusb
usbreset 001/002 # Number 001/002  ID 2886:0059  seeed-xiao-s3
lsusb
usbreset 2886:0059 # 2nd attempt
lsusb