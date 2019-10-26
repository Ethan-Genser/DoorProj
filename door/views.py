#!/usr/bin/env python3

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

import time
import subprocess

RESPONSE_STRING = "Welcome back!"
RUN_CMD = "sudo python3 open.py"

# Opens Door
def open(self):

    # Initializes HTTP response objhect
    httpResponse = HttpResponse(RESPONSE_STRING)
    httpResponse['ExitStatus'] = 1

    # Calls python script to run the motors
    subprocess.call(RUN_CMD, shell=True)

    # Returns HTTP response object
    httpResponse['ExitStatus'] = 0          # 0-Successful, 1-Unsuccessful
    httpResponse['DoorStatus'] = 0          # 0-Closed, 1-Operating
    httpResponse['RoommateStatus'] = 0      # 0-In, 1-Away, 2-DoNotDisturb, 3-Sleeping
    return httpResponse
