#!/usr/bin/env python

from datetime import datetime
import logging
import RPi.GPIO as GPIO

now = datetime.now()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.LOW)
