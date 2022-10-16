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

#import logging as log

import os
import sys
import time
import threading

def mission_bridge(eve):
    eve.calibrategs()
    eve.moveblock(25,25,550)
    eve.moveblock(-35,-35,70)
    eve.moveblock(-10,10,45)
    #eve.aaasetup()
    eve.moveblock(40,40,410)
    eve.moveblock(10,-10,90)
    eve.moveblock(20,20,130)

    for x in range (3): 
        #eve.aaasetup
        eve.moveblock(20,20,60)
        time.sleep(0.35)
        eve.moveblock(-20,-20,50)

    #eve.moveblock(20,20,50)
    #time.sleep(0.35)
    #eve.aaasetup()
    #eve.moveblock(-20,-20,50)
    #eve.moveblock(20,20,50)
    #time.sleep(0.35)
    #eve.aaasetup()