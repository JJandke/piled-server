#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from https://github.com/JJandke
# 16 = Red, 20 = Green, 21 blue
#
# This script is not used for Piled and is just an RGB version of the Multistrobe script.
# To enable it, you still need to create a corresponding php script and then call it from the client.
# This requires another button in the app.
# Since the script cannot be called by the client at the moment, there is yet no way implemented to terminate it.
#

from datetime import datetime
from time import sleep
import logging
import pigpio
import random
import codecs
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
speed = 0.3  # The smaller the variable, the faster the colors will change.
log_time = now.strftime("%a-%d.%m.%Y-%H:%M:%S ")


def red():
    pi.set_PWM_dutycycle(16, 255)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, 0)


def green():
    pi.set_PWM_dutycycle(16, 0)
    pi.set_PWM_dutycycle(20, 255)
    pi.set_PWM_dutycycle(21, 0)


def blue():
    pi.set_PWM_dutycycle(16, 0)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, 255)


def run():
    with codecs.open("/home/pi/.server/strobe.txt", "w") as f:
        f.close()
    while os.path.exists("/home/pi/.server/strobe.txt"):
        random.choice(colors)()
        sleep(speed)


colors = [red, green, blue]

try:
    if os.path.exists("/home/pi/.server/fade.txt"):
        os.remove("/home/pi/.server/fade.txt")
        logging.info("{0}Set color: RGBstrobe".format(log_time))
        sleep(0.5)
        run()
    elif os.path.exists("/home/pi/.server/multistrobe.txt"):
        os.remove("/home/pi/.server/multistrobe.txt")
        logging.info("{0}Set color: RGBstrobe".format(log_time))
        sleep(0.5)
        run()
    else:
        logging.info("{0}Set color: RGBstrobe".format(log_time))
        sleep(0.5)
        run()

except Exception as e:
    logging.debug("{0}Could not start RGBstrobe: {1}".format(log_time, e))
