#!/usr/bin/env python3



from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import MoveTank
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, SpeedPercent, follow_for_ms
#from ev3dev2.wheel import Wheel
from ev3dev2.sensor import INPUT_1, INPUT_2,INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor

import logging as log


import os
import sys
import time


from globals import *
from missions import *
from myblocks import EveTank

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
            left_motor_port = OUTPUT_C,
            right_motor_port = OUTPUT_B,
            Wheel_Dia = Wheel_Dia,
            csl_port = INPUT_1, 
            csr_port = INPUT_4, # left and right color sensor
            gy_port = INPUT_2,
            turret_port = OUTPUT_A,
            attach_port = OUTPUT_D,
            )
    
    
    #menuing system goes here
    mission04(eve)
    #mission01(eve)

    def calibratecs(self,speed=20, time=5):
        self.csl_min = 50
        self.csl_max = 50
        self.csr_min = 50
        self.csr_max = 50

        # dont start until button is pushed!!

        end_time = time.time() + time
        #DB Reads mins and maxs of both sensors and chages it based on what it read
        self.on(speed,speed)
        while time.time() < end_time:
            readl = self.csl.value()
            readr = self.csr.value()
            if self.csl_max < readl:
                self.csl_max = readl
            if self.csl_min > readl:
                self.csl_min = readl
            if self.csr_max < readr:
                self.csr_max = readr
            if self.csr_min > readr:
                self.csr_min = readr
 
        self.off(self)

        self.csl_mid = (self.csl_max - self.csl_min) / 2
        self.csr_mid = (self.csr_max - self.csr_min) / 2
    
    def line_finder(self,left_or_rightsensor, white_or_black):
        #pseudo code
        #chose which sensor to use 
        #chose what color to find
        #
        while left_or_rightsensor != white_or_black:
            self.on(20,20) 
        else:
            self.off
            
    #calibratecs(eve)
            
    #line_finder(eve,eve.csl,0)

    
# if:
               # self.left_or_rightsensor.value() ==
    

    debug_print('Main  Done')
 #   time.sleep(5)


if __name__ == '__main__':
    Main()

