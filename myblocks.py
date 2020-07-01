from ev3dev2.motor import MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.wheel import Wheel

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
# MOVE BLOCK
wheels = MoveTank(OUTPUT_B, OUTPUT_C) 
#left_speed=
#circumference=
#right_speed=
'''Format
wheels.on_for_rotations(left_speed,right_speed, rotations, brake=True, block=True)
'''
wheels.on_for_rotations(5)
'''
How to add pi
import math
math.pi will print pi and add it as a variable  

