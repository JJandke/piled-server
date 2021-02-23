# /usr/bin/python3
# -*- coding: utf-8 -*-
# from https://github.com/JJandke
#

from datetime import datetime
import RPi.GPIO as GPIO
import logging
import os

# Create log file for this script
# Running the script via cronjob at boot will delete the log file each time to save disk space and keep the file more organized.
if os.path.isfile("/home/pi/log/piled/power_on.log"):
    os.remove("/home/pi/log/piled/power_on.log")
    f = open("/home/pi/log/piled/power_on.log", "x")
    f.close()
else:
    f = open("/home/pi/log/piled/power_on.log", "x")
    f.close()

logging.basicConfig(filename="/home/pi/log/piled/power_on.log", level=logging.DEBUG)
now = datetime.now()
log_time = now.strftime("%a-%d.%m.%Y-%H:%M:%S ")

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(12,GPIO.OUT)
    GPIO.output(12,GPIO.LOW)
    logging.info("{0}Power On".format(log_time))

except Exception as e:
    logging.debug("{0}Could not power On: {1}".format(log_time, e))
