#!/usr/bin/python3
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
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.LOW)
    logging.info("{0}Power off".format(log_time))

except Exception as e:
    logging.debug("{0}Could not power off: {1}".format(log_time, e))
