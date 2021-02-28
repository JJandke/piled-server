# /usr/bin/python3
# -*- coding: utf-8 -*-
# from https://github.com/JJandke
#

from datetime import datetime
from time import sleep
import logging
import pigpio
import os

# Create log file if it does not exist.
if not os.path.isfile("/home/pi/log/piled.log"):
    f = open("/home/pi/log/piled.log", "x")
    f.close()
else:
    pass

logging.basicConfig(filename="/home/pi/log/piled.log", level=logging.DEBUG)
pi = pigpio.pi()
now = datetime.now()
log_time = now.strftime("%a-%d.%m.%Y-%H:%M:%S ")

# It checks if the files exist. If they do, they will be deleted. If they do not exist, fade.py or strobe.py will stop if they are running.
try:
    if os.path.exists("/home/pi/.server/fade.txt"):
        os.remove("/home/pi/.server/fade.txt")
    if os.path.exists("/home/pi/.server/multistrobe.txt"):
        os.remove("/home/pi/.server/multistrobe.txt")

    # Waiting one second is necessary, otherwise requested color will be overwritten by the last fade command.
    sleep(0.5)
    pi.set_PWM_dutycycle(16, 255)   # red
    pi.set_PWM_dutycycle(20, 255)   # green
    pi.set_PWM_dutycycle(21, 255)   # blue
    logging.info("{0}Set color: White".format(log_time))

except Exception as e:
    logging.debug("{0}Could not set color to White: {1}".format(log_time, e))
