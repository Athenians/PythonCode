from ev3dev2.motor import MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.wheel import Wheel

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
# MOVE BLOCK
mtank = MoveTank(OUTPUT_B, OUTPUT_C) 
def moveblock(mtank,speed,distance):
    rotations = distance / 315
    mtank.on_for_rotations(speed, speed, rotations, brake=True, block=True)


