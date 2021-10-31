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

def calibrate(eve):
    eve.calibrategs()
    eve.calibratecs(10,2)

def mission_bridge(eve):
    eve.aaasetup()
    eve.calibrategs()
    eve.find_line_2()
    #add attachment or stick to drop bridge
    eve.left_motor.position = 0
    eve.right_motor.position = 0 
    try:
        eve.athfollow_line(
            #kp=2, ki=0.060, #kd=3,
            kp=4, ki=0.06, kd=3,         # use this for change of directions speed = 10       
            #kp=2, ki=0.000, #kd=0,           # use this for speed=20 on straight lines
            speed=SpeedPercent(5),
            cs_for_line = eve.csr,            
            follow_left_edge= True,
            sleep_time=0.002,
            #follow_for=follow_until_line,cs_for_until = eve.csl, wb = 'b',tolerence=2
            follow_for = follow_for_distance,distance = 1300
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise

    eve.line_finder(10,10,'l','w')
    eve.turnblock(15,110)

    #food package dropped during this
    eve.moveblock(15,15,380)
    eve.motor_mover(45,12,eve.turret)
    eve.motor_mover(10,0.7,eve.attach)
    eve.motor_mover(45,-12,eve.turret)
    eve.motor_mover(10,0.25,eve.attach)

    '''
    eve.turnblock(15,178)
    eve.aaasetup()
    #add attachment or stick to drop bridge
    eve.left_motor.position = 0
    eve.right_motor.position = 0 
    try:
        eve.athfollow_line(
            #kp=2, ki=0.060, #kd=3,
            kp=3, ki=0.00, kd=0,         # use this for change of directions speed = 10       
            #kp=2, ki=0.000, #kd=0,           # use this for speed=20 on straight lines
            speed=SpeedPercent(12),
            cs_for_line = eve.csl,            
            follow_left_edge=False,
            sleep_time=0.002,
            #follow_for=follow_until_line,cs_for_until = eve.csl, wb = 'b',tolerence=2
            follow_for = follow_for_distance,distance = 1450
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise
        '''

   # eve.moveblock(20,20,400)

def mission_unload_cargo_plane(eve):
    eve.aaasetup()
    eve.calibrategs()
    eve.moveblock(10,10,1000)
    eve.turnblock(10,90)



    
    eve.motor_mover(10,0.75,eve.turret)
    eve.turnblock(10,20)
    eve.moveblock(10,10,-280)
    eve.turnblock(10,-145)
    eve.moveblock(30,30,550)