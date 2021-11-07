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
            follow_for = follow_for_distance,distance = 1000
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise

    eve.line_finder(10,10,'l','w')
    eve.aaasetup()
    eve.moveblock(5,5,35)
    eve.moveblock(5,5,-35)
    eve.aaasetup()
    eve.turnblock(15,110)
    eve.aaasetup()
    #food package dropped during this
    '''
    x = threading.Thread(target = eve.motor_mover, args = (45,9,eve.turret,) )
    y = threading.Thread(target = eve.motor_mover, args = (15,1.07,eve.attach,))

    x.start()
    y.start()

    x.join()
    y.join()
    '''
    eve.motor_mover(45,6,eve.turret)
    eve.motor_mover(15,0.7,eve.attach)
    eve.aaasetup()
    eve.moveblock(15,15,380)
    eve.aaasetup()
    eve.moveblock(20,20,-400)
    eve.aaasetup()
    eve.motor_mover(55,-3,eve.turret)
    eve.motor_mover(7,0.15,eve.attach)
    eve.aaasetup()
    eve.moveblock(20,20,490)
    eve.aaasetup()
    eve.motor_mover(45,-3,eve.turret)
    eve.motor_mover(15,-0.85,eve.attach)

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
        '''

    #eve.moveblock(20,20,-200)
    eve.turnblock(10,90)

def mission_unload_cargo_plane(eve):
    eve.aaasetup()
    eve.calibrategs()
    eve.motor_mover(40,2.2,eve.turret)
    eve.moveblock(15,15,600)
    eve.motor_mover(15,1.5,eve.attach)
    #eve.aaasetup()
    eve.motor_mover(15,-1.5,eve.attach)
    eve.motor_mover(45,-2.2,eve.turret)
    eve.moveblock(10,10,-80)
    #eve.aaasetup()
    #eve.turnblock(10,45)
    #eve.motor_mover(15,1.0,eve.attach)
    #eve.moveblock(15,15,100)
    #eve.motor_mover(15,-1.0,eve.attach)
    #eve.moveblock(15,15,-90)
    eve.turnblock(10,90)
    eve.moveblock(30,30,-500)


def mission_cargo_circle(eve):
    eve.aaasetup()
    eve.calibrategs()
    eve.moveblock(15,15,150)
    eve.turnblock(15,90)
    eve.moveblock(15,15,1050)
    eve.turnblock(15,-90)
    eve.moveblock(15,15,25)
    eve.moveblock(15,15,-450)
    eve.moveblock(15,15,250)
    eve.turnblock(15,-90)
    eve.moveblock(15,15,1300)
