#!/usr/bin/env python3

from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.wheel import Wheel
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor

import logging as log


import os
import sys
import time


from aaasetup import aaasetup
from globals import *


btn = Button()
sound = Sound()

turret = Motor(OUTPUT_A)
attach = Motor(OUTPUT_D)



# logging
log.basicConfig(level=log.DEBUG, format="%(asctime)s %(levelname)5s: %(message)s")
#log = logging.getLogger(__name__)

    # logging.basicConfig(filename='mylog.log')
    # log = getLogger(__name__)
    # log.setLevel(logging.DEBUG)

# state constants
ON = True
OFF = False



class MCTire(Wheel):
    """
    part number 56145
    comes in set 31313
    """
    def __init__(self):
        Wheel.__init__(self, 100.3, 17)


# def left(state):
#     if state:
#         debug_print('Left button pressed')
#         turret.on(speed=45)
#     else:
#         debug_print('Left button released')
#         turret.off()
#     return 0
   
# def right(state):  # neater use of 'if' follows:
#     if state:
#         debug_print('right button pressed')
#         turret.on(speed=-45)
#     else:
#         debug_print('right button released')
#         turret.off()

#     return 0
 
# def up(state):
#     if state:
#         debug_print('Up button pressed')
#         attach.on(speed=5)
#     else:
#         debug_print('Up button released')
#         attach.off()
#     return 0
   
# def down(state):
#     if state:
#         debug_print('Down button pressed')
#         attach.on(speed=-5)
#     else:
#         debug_print('Down button released')
#         attach.off()
#     return 0

# def enter(state):
#     if state:
#         debug_print('Enter button pressed')
#     else:
#         debug_print('Enter button released')


# def aaasetup():

#     debug_print('aaasetup')
#     print('hit a button')  
#     btn.on_left = left
#     btn.on_right = right
#     btn.on_up = up
#     btn.on_down = down
#     btn.on_enter = enter

#     while True:
#         #debug_print(btn.buttons_pressed)
#         if btn.check_buttons(buttons=['enter']):
#             debug_print('enter button hit')
#             break
#         btn.process()
#         time.sleep(0.01)


def Main():
    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    debug_print('Main')

    aaasetup()

    debug_print('Done')
 #   time.sleep(5)


if __name__ == '__main__':
    Main()

    