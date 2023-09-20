#!/usr/bin/env python3



#from ev3dev2.button import Button
from ev3dev2.sound import Sound
#from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import MoveTank, LineFollowErrorTooFast, follow_for_forever
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, SpeedPercent, follow_for_ms
#from ev3dev2.wheel import Wheel
#from ev3dev2.sensor import INPUT_1, INPUT_2,  INPUT_4
#from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.led import Leds
from myblocks import EveTank, follow_until_line, follow_for_distance
from globals import debug_print
#import logging as log

import os
import sys
import time
import threading

def mission_pickle_dragon(eve):
    eve.aaasetup()
    eve.motor_mover(50,1,eve.attach)
    eve.moveblock(30,30,190)
    eve.moveblock(-10,10,30)
    eve.moveblock(30,30,130)
    eve.moveblock(10,-10,30)
    eve.moveblock(-40,-40,320)

def M02(eve):
    eve.aaasetup()    
    eve.motor_mover(40,1.25,eve.attach)
    eve.moveblock(20,20,600)
    for x in range (2):
        eve.motor_mover(20,-1.5,eve.attach)
        eve.motor_mover(20,1.5,eve.attach)