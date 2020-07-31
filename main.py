#!/usr/bin/env python3



from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import MoveTank, MoveDifferential
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, SpeedPercent, follow_for_ms
from ev3dev2.wheel import Wheel
from ev3dev2.sensor import INPUT_1, INPUT_2,INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor

import logging as log


import os
import sys
import time


from globals import *
from missions import *

btn = Button()
sound = Sound()



#turret = Motor(OUTPUT_A)
#attach = Motor(OUTPUT_D)



# logging
log.basicConfig(level=log.DEBUG, format="%(asctime)s %(levelname)5s: %(message)s")
#log = logging.getLogger(__name__)

    # logging.basicConfig(filename='mylog.log')
    # log = getLogger(__name__)
    # log.setLevel(logging.DEBUG)

# state constants
ON = True
OFF = False


def Main():
    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    debug_print('Main  Start')


    mission01()

    debug_print('Main  Done')
 #   time.sleep(5)


if __name__ == '__main__':
    Main()

