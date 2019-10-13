#!/usr/bin/env python3

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

import time
import subprocess

motor_kit = MotorKit()

# Reeling in the door handle for 2.4 seconds
start_time = time.time()
current_time = start_time
while (current_time - start_time <= 2.2):
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
while (current_time - start_time <= 2.1):
    motor_kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    motor_kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    current_time = time.time()

# Releases motor coils
motor_kit.stepper1.release()
motor_kit.stepper2.release()
