# /usr/bin/python3
# -*- coding: utf-8 -*-
# from https://github.com/JJandke
#

from datetime import datetime
from time import sleep
import logging
import pigpio
import os

# Create log file for this script.
if not os.path.isfile("/home/pi/log/piled.log"):
    f = open("/home/pi/log/piled.log", "x")
    f.close()
else:
    pass

logging.basicConfig(filename="/home/pi/log/piled.log", level=logging.DEBUG)
pi = pigpio.pi()
now = datetime.now()
log_time = now.strftime("%a-%d.%m.%Y-%H:%M:%S ")

try:
    if os.path.exists("/home/pi/.server/fade.txt"):
        os.remove("/home/pi/.server/fade.txt")
    if os.path.exists("/home/pi/.server/multistrobe.txt"):
        os.remove("/home/pi/.server/multistrobe.txt")
    sleep(1)
    pi.set_PWM_dutycycle(21, 0)     # red
    pi.set_PWM_dutycycle(20, 0)     # green
    pi.set_PWM_dutycycle(16, 0)     # blue
    logging.info("{0}Set color: Black".format(log_time))

except Exception as e:
    logging.debug("{0}Could not set color to Black: {1}".format(log_time, e))
