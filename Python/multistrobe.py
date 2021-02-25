# /usr/bin/python3
# -*- coding: utf-8 -*-
# from https://github.com/JJandke
# 16 = Red, 20 = Green, 21 blue
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


def orange():
    pi.set_PWM_dutycycle(16, 255)
    pi.set_PWM_dutycycle(20, 15)
    pi.set_PWM_dutycycle(21, 0)


def turquoise():
    pi.set_PWM_dutycycle(16, 0)
    pi.set_PWM_dutycycle(20, 20)
    pi.set_PWM_dutycycle(21, 255)


def purple():
    pi.set_PWM_dutycycle(16, 255)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, 50)


def yellow():
    pi.set_PWM_dutycycle(16, 255)
    pi.set_PWM_dutycycle(20, 60)
    pi.set_PWM_dutycycle(21, 0)


def run():
    with codecs.open("/home/pi/.server/multistrobe.txt", "w") as f:
        f.close()
    while os.path.exists("/home/pi/.server/multistrobe.txt"):
        random.choice(colors)()
        sleep(speed)


colors = [red, green, blue, orange, turquoise, purple, yellow]

try:
    if os.path.exists("/home/pi/.server/fade.txt"):
        os.remove("/home/pi/.server/fade.txt")
        logging.info("{0}Set color: Multistrobe".format(log_time))
        sleep(1)
        run()
    else:
        logging.info("{0}Set color: Multistrobe".format(log_time))
        sleep(1)
        run()

except Exception as e:
    logging.debug("{0}Could not start Multistrobe: {1}".format(log_time, e))
