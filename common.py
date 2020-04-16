#!/usr/bin/env python3


from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import MoveTank, MoveDifferential
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.wheel import Wheel
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor

import logging as log


import os
import sys
import time

from globals import *


class MCTire(Wheel):
    """
    part number 56145
    comes in set 31313
    """
    def __init__(self):
        Wheel.__init__(self, 100.3, 17)


def Calibrate():
    gs = GyroSensor(INPUT_2)

    debug_print('GS Calibration begin')
    for x in range(2):
        gs.mode = 'GYRO-RATE'
        gs.mode = 'GYRO-ANG'
        time.sleep(.5)

    gsnow = gs.angle
    debug_print('GS Calibration finish ' + str(gsnow))

def initmotors():

    lw = Motor(OUTPUT_C)
    rw = Motor(OUTPUT_B)

    # for x in (lw,rw):
    #     x.polarity = 'inversed'
    #     x.ramp_up_sp = 2000
    #     x.ramp_down_sp = 2000

    # lw.polarity = 'inversed'
    # rw.polarity = 'inversed'

    lw.ramp_up_sp = 2000
    rw.ramp_up_sp = 2000

    lw.ramp_down_sp = 1000
    rw.ramp_down_sp = 1000

    global mdiff
    global mtank

    mdiff = MoveDifferential(OUTPUT_C, OUTPUT_B, MCTire, 129.3)
    mtank = MoveTank(OUTPUT_C, OUTPUT_B)
    mtank.gyro = GyroSensor()
    mdiff.set_polarity('inversed')