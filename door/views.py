#!/usr/bin/env python3

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time

# Opens Door
def open(self):
    motor_kit = MotorKit()

    # Reeling in the door handle for 2.7 seconds
    start_time = time.time()
    current_time = start_time
    while (current_time - start_time <= 2.5):
        motor_kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        motor_kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        current_time = time.time()

    # Pauses for 5 seconds to give the user time to open the door
    start_time = time.time()
    current_time = start_time
    while (current_time - start_time <= 5):
        current_time = time.time()

    # Unreels the door handle for 2.5 seconds
    start_time = time.time()
    current_time = start_time
    while (current_time - start_time <= 2.3):
        motor_kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        motor_kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        current_time = time.time()

    # Releases motor coils
    motor_kit.stepper1.release()
    motor_kit.stepper2.release()
