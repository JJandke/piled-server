#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from https://github.com/JJandke
# 16 = Red, 20 = Green, 21 blue
#

from datetime import datetime
from time import sleep
import logging
import pigpio
import sys
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
speed = 0.1     # The smaller the variable, the faster the colors will change.
log_time = now.strftime("%a-%d.%m.%Y-%H:%M:%S ")


def run():
    while os.path.exists("/home/pi/.server/fade.txt"):              # Check if script is allowed to be executed. (Only if fade.txt exists)
        col_b1 = 255
        col_r1 = 0
        col_r2 = 255
        col_g2 = 0
        col_g3 = 255
        col_b3 = 0
        while col_b1 > -1 and col_r1 < 255:
            pi.set_PWM_dutycycle(21, col_b1)
            pi.set_PWM_dutycycle(16, col_r1)
            col_b1 = col_b1 - 1
            col_r1 = col_r1 + 1
            if not os.path.exists("/home/pi/.server/fade.txt"):     # Check if script is allowed to be executed. (Only if fade.txt exists)
                sys.exit(0)
            sleep(speed)                                            # sleep (speed) seconds. So a smaller number means faster fading.
        while col_r2 > -1 and col_g2 < 255:
            pi.set_PWM_dutycycle(16, col_r2)
            pi.set_PWM_dutycycle(20, col_g2)
            col_r2 = col_r2 - 1
            col_g2 = col_g2 + 1
            if not os.path.exists("/home/pi/.server/fade.txt"):
                sys.exit(0)
            sleep(speed)
        while col_g3 > -1 and col_b3 < 255:
            pi.set_PWM_dutycycle(20, col_g3)
            pi.set_PWM_dutycycle(21, col_b3)
            col_g3 = col_g3 - 1
            col_b3 = col_b3 + 1
            if not os.path.exists("/home/pi/.server/fade.txt"):
                sys.exit(0)
            sleep(speed)


try:
    # Set all channels to 0 so that the colors are displayed correctly from the start.
    pi.set_PWM_dutycycle(16, 0)
    pi.set_PWM_dutycycle(20, 0)
    pi.set_PWM_dutycycle(21, 0)

    # Create file to signal that the script is running.
    if not os.path.exists("/home/pi/.server/fade.txt"):
        os.mknod("/home/pi/.server/fade.txt")

    # Terminate strobe if it is running.
    if os.path.exists("/home/pi/.server/multistrobe.txt"):
        os.remove("/home/pi/.server/multistrobe.txt")
        logging.info("{0}Set color: Fade".format(log_time))
        sleep(0.5)
        run()
    else:
        logging.info("{0}Set color: Fade".format(log_time))
        sleep(0.5)
        run()

except Exception as e:
    logging.debug("{0}Could not start fading: {1}".format(log_time, e))
