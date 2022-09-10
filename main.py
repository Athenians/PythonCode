#!/usr/bin/env python3



from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import MoveTank,LineFollowErrorTooFast
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, SpeedPercent, follow_for_ms, follow_for_forever
#from ev3dev2.wheel import Wheel
from ev3dev2.sensor import INPUT_1, INPUT_2,INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.led import Leds
import logging as log


import os
import sys
import time


from globals import *
from missions import *
from myblocks import EveTank, follow_until_line
from menu import Menu
import pickle 

btn = Button()
sound = Sound()


# logging
#log.basicConfig(level=log.DEBUG, format="%(asctime)s %(levelname)5s: %(message)s")
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
    Wheel_Dia = 81.6           #68 for other robot
    eve = EveTank(
            left_motor_port = OUTPUT_C,
            right_motor_port = OUTPUT_D,
            Wheel_Dia = Wheel_Dia,
            csl_port = INPUT_2, 
            csr_port = INPUT_1, # left and right color sensor
            gy_port = INPUT_3,
            left_medium_port = OUTPUT_B,
            right_medium_port = OUTPUT_A,
            )


    #menuing system goes here
    menu = Menu()
    menu.runmenu(eve)

    debug_print('Main  Done')

 #   time.sleep(5)

if __name__ == '__main__':
    Main()



'''
dans robot info
wheel diameter = 81.6
left_motor_port = OUTPUT_C,
            right_motor_port = OUTPUT_D,
            Wheel_Dia = Wheel_Dia,
            csl_port = INPUT_2, 
            csr_port = INPUT_1, # left and right color sensor
            gy_port = INPUT_3,
            left_medium_port = OUTPUT_B,
            right_medium_port = OUTPUT_A,
eve robot info
Wheel_Dia = 103.8           #68 for other robot
    eve = EveTank(
            left_motor_port = OUTPUT_B,
            right_motor_port = OUTPUT_C,
            Wheel_Dia = Wheel_Dia,
            csl_port = INPUT_2, 
            csr_port = INPUT_3, # left and right color sensor
            gy_port = INPUT_4,
            left_medium_port = OUTPUT_D,
            right_medium_port = OUTPUT_A,
            )
'''