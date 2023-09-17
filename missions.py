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
    eve.motor_mover(15,1,eve.attach)
    eve.moveblock(30,30,190)
    eve.moveblock(-30,30,30)
    eve.moveblock(30,30,130)
    eve.moveblock(30,-30,30)
    eve.moveblock(-60,-60,320)
    eve.motor_mover(20,-1,eve.attach)