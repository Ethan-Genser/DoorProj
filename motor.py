from adafruit_motorkit import MotorKit
import time

def main():
    motor_kit = MotorKit()
    start_time = time.time()
    current_time = start_time
    while (current_time - start_time <= 3):
        motor_kit.stepper1.onestep()
        current_time = time.time()

if(__name__=="__main__"):main()
