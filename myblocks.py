from ev3dev2.motor import MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.wheel import Wheel
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
# MOVE BLOCK
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C) 
#no matter what speed always must be a negative integer
tank_pair.on(left_speed=-15, right_speed=-15)