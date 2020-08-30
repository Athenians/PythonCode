#!/usr/bin/env python3



#from ev3dev2.button import Button
#from ev3dev2.sound import Sound
#from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import MoveTank
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, SpeedPercent, follow_for_ms
#from ev3dev2.wheel import Wheel
#from ev3dev2.sensor import INPUT_1, INPUT_2,  INPUT_4
#from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor

#import logging as log

import os
import sys
import time


def mission01(eve):
    eve.calibrategs()
    eve.moveblock(25,25,30)
    eve.turnblock(10,80)
    eve.moveblock(25,25,1650)
    eve.turnblock(10,-80)


def mission02(eve):

    eve.calibrategs()
    for x in range(4):
        eve.moveblock(25,25,400)
        eve.turnblock(10,90,error_margin=0)

    #eve.moveblock(25,25,1500)


def mission03(eve):
    eve.calibrategs()
    eve.moveblock(25,25,10)
    eve.turnblock(10,75)
    eve.moveblock(25,25,800)
    eve.moveblock(7,7,60)
    for x in range (1):
       eve.moveblock(7,7,-10)
       eve.moveblock(7,7,70)    
    for x in range(6):
        eve.moveblock(7,7,-20)
        eve.moveblock(7,7,70)
    for x in range (1):
        eve.moveblock(7,7,-20)
        eve.moveblock(7,7,80)

    eve.moveblock(60,60,-1360)
    

def mission04(eve):
    eve.calibrategs

def mission05(eve):
    eve.moveblock(20,20,50)
    eve.turnblock(10,80)
    eve.moveblock(20,20,670)
    eve.turnblock(10,70)
    eve.moveblock(15,15,220)
    eve.turnblock(10,130)
    eve.moveblock(40,40,680)
