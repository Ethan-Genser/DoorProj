# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from adafruit_motorkit import MotorKit
import time

# Opens Door
def open(self):
    motor_kit = MotorKit()
    start_time = time.time()
    current_time = start_time
    while (current_time - start_time <= 3):
        motor_kit.stepper1.onestep()
        current_time = time.time()
