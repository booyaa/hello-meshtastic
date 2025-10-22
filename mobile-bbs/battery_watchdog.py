#!/usr/bin/env python

import logging
import os
import subprocess
import time


sleep_in_seconds = os.environ.get("BATTERY_CHECK_INTERVAL", 60)
logging_level = os.environ.get("LOGGING_LEVEL", "INFO").upper()

logging.basicConfig(level=logging_level)

logging.info(f"Battery check interval set to {sleep_in_seconds} seconds.")
logging.info(f"Logging level set to {logging_level}.")
# loop the rest of this code to run every 60 seconds
while True:
    battery_info = subprocess.check_output(["./battery_meter"]).decode("utf-8").strip()
    logging.debug(f"Battery capacity: {battery_info}%")

    if int(battery_info) <= 5:
        logging.warning("Battery level is below 5%! Shutting down!")
        subprocess.Popen(["shutdown", "-h", "now"])

    # wait for the specified amount of time before checking again
    time.sleep(int(sleep_in_seconds))
