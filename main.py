#!/usr/bin/env python3



from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import MoveTank,LineFollowErrorTooFast
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, SpeedPercent, follow_for_ms, follow_for_forever
#from ev3dev2.wheel import Wheel
from ev3dev2.sensor import INPUT_1, INPUT_2,INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor

import logging as log


import os
import sys
import time


from globals import *
from missions import *
from myblocks import EveTank, follow_until_line
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
    Wheel_Dia = 100.3           #68 for otther robot
    
    eve = EveTank(
            left_motor_port = OUTPUT_D,
            right_motor_port = OUTPUT_B,
            Wheel_Dia = Wheel_Dia,
            csl_port = INPUT_1, 
            csr_port = INPUT_4, # left and right color sensor
            gy_port = INPUT_2,
            turret_port = OUTPUT_A,
            attach_port = OUTPUT_C,
            )


#    mission_Row_Machine(eve)

  #  mission_bench(eve)
    
    mission_basket(eve)
  
    #menuing system goes here
    
    # mission01(eve)


     

    debug_print('Main  Done')
 #   time.sleep(5)


if __name__ == '__main__':
    Main()

