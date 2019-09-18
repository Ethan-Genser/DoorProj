#!/usr/bin/env python3

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import time

# Opens Door
def open(self):
    httpResponse = HttpResponse("Welcome back!")
    httpResponse['ExitStatus'] = 1

    motor_kit = MotorKit()

    # Reeling in the door handle for 2.4 seconds
    start_time = time.time()
    current_time = start_time
    while (current_time - start_time <= 2.4):
        motor_kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        motor_kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        current_time = time.time()

    # Pauses for 5 seconds to give the user time to open the door
    start_time = time.time()
    current_time = start_time
    while (current_time - start_time <= 5):
        current_time = time.time()

    # Unreels the door handle for 2.2 seconds
    start_time = time.time()
    current_time = start_time
    while (current_time - start_time <= 2.2):
        motor_kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        motor_kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        current_time = time.time()

    # Releases motor coils
    motor_kit.stepper1.release()
    motor_kit.stepper2.release()

    # Returns HTTP response object
    httpResponse['ExitStatus'] = 0          # 0-Successful, 1-Unsuccessful
    httpResponse['DoorStatus'] = 0          # 0-Closed, 1-Operating
    httpResponse['RoommateStatus'] = 0      # 0-In, 1-Away, 2-DoNotDisturb, 3-Sleeping
    return httpResponse
