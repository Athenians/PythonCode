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
    eve.moveblock(5,5,35)
    eve.moveblock(5,5,-35)
    eve.turnblock(15,110)
    #food package dropped during this
    eve.motor_mover(55,2.85,eve.turret)
    eve.motor_mover(15,1.0,eve.attach)
    eve.moveblock(20,20,380)
    eve.motor_mover(55,-2.85,eve.turret)
    eve.moveblock(20,20,-452.5)
    eve.motor_mover(55,1.8,eve.turret)
    eve.motor_mover(15,0.25,eve.attach)
    eve.moveblock(20,20,480)
    eve.moveblock(20,20,-50)
    eve.motor_mover(15,-0.85,eve.attach)
    eve.motor_mover(55,-1.65,eve.turret)
    eve.turnblock(10,90)
    eve.moveblock(20,20,255)
    eve.turnblock(10,35)
    eve.motor_mover(15,0.35,eve.attach)
    eve.motor_mover(55,-1.0,eve.turret)
    eve.moveblock(20,20,475)
    eve.turnblock(10,120)
    eve.moveblock(20,20,157.5)
    eve.moveblock(20,20,-175)
    eve.turnblock(5,45)
    eve.moveblock(15,15,-150)
    eve.turnblock(5,-45)
    eve.moveblockk(20,20,-140)

 
def mission_unload_cargo_plane(eve):
    eve.aaasetup()
    eve.motor_mover(55,1.92,eve.turret)
    eve.moveblock(20,20,615)
    eve.motor_mover(15,1.83,eve.attach)
    eve.motor_mover(15,-1.83,eve.attach)
    eve.motor_mover(55,-1.92,eve.turret)
    eve.moveblock(10,10,-80)
    eve.turnblock(10,90)
    eve.moveblock(30,30,-500)


def mission_cargo_circle(eve):
    eve.aaasetup()
    eve.moveblock(20,20,225)
    eve.turnblock(5,80)    
    eve.moveblock(20,20,1025)
    eve.moveblock(0,30,220)
    eve.motor_mover(15,1.0,eve.attach)
    eve.motor_mover(55,2.0,eve.turret)
    eve.moveblock(20,20,-100)
    eve.turnblock(15,80)
    eve.moveblock(35,35,-1450)
    eve.motor_mover(15,-0.5,eve.attach)
    eve.motor_mover(55,-2.0,eve.turret)    
    eve.turnblock(10,90)

