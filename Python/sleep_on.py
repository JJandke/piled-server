#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from https://github.com/JJandke
#

from datetime import datetime
import RPi.GPIO as GPIO
import logging
import os

# Create log file if it does not exist.
if not os.path.isfile("/home/pi/log/piled.log"):
    f = open("/home/pi/log/piled.log", "x")
    f.close()
else:
    pass

logging.basicConfig(filename="/home/pi/log/piled.log", level=logging.DEBUG)
now = datetime.now()
log_time = now.strftime("%a-%d.%m.%Y-%H:%M:%S ")

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    logging.info("{0}Sleep on".format(log_time))

except Exception as e:
    logging.debug("{0}Could not set sleep to on: {1}".format(log_time, e))
