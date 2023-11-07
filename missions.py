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
from globals import debug_print
#import logging as log

import os
import sys
import time
import threading

def M001(eve):
    #align to AN8
    #puts 2 orange people in the skate park
    eve.aaasetup()
    eve.moveblock(30,30,200)
    eve.line_finder(10,10,'r','b')

    eve.left_motor.position = 0
    eve.right_motor.position = 0 
    try:
        eve.athfollow_line(
            #kp=2, ki=0.060, #kd=3,
            kp=4, ki=0.06, kd=3,         # use this for change of directions speed = 10       
            #kp=2, ki=0.000, #kd=0,           # use this for speed=20 on straight lines
            speed=SpeedPercent(10),
            cs_for_line = eve.csr,            
            follow_left_edge= True,
            sleep_time=0.002,
             follow_for=follow_until_line,cs_for_until = eve.csl, wb = 'b',tolerence=2
            #follow_for = follow_for_distance,distance = 1000
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise
    eve.moveblock(40,20,210)
    eve.motor_mover(50,2,eve.attach)
    eve.moveblock(-40,-20,220)
 

    x = threading.Thread(target = eve.moveblock, args = (-45,-40,680,) )
    y = threading.Thread(target = eve.motor_mover, args = (50,-2,eve.attach,))

    x.start()
    y.start()

    x.join()
    y.join()

def M00(eve):
    # align to AN7
    # Put 2 orange people into cinema
    eve.aaasetup()
    eve.moveblock(30,30,380)
    eve.motor_mover(50,1,eve.attach)
    x = threading.Thread(target = eve.moveblock, args = (-30,-30,370,) )
    y = threading.Thread(target = eve.motor_mover, args = (50,-1,eve.attach,))

    x.start()
    y.start()

    x.join()
    y.join()


def M01(eve):
    # align to AN1
    # M01 3D Cinema
    eve.aaasetup()

    x = threading.Thread(target = eve.moveblock, args = (30,30,190,) )
    y = threading.Thread(target = eve.motor_mover, args = (50,1,eve.attach,))

    x.start()
    y.start()

    x.join()
    y.join()

    eve.moveblock(-10,10,30)
    eve.moveblock(30,30,130)
    eve.moveblock(10,-10,30)

    x = threading.Thread(target = eve.moveblock, args = (-40,-40,320,) )
    y = threading.Thread(target = eve.motor_mover, args = (50,-1,eve.attach,))

    x.start()
    y.start()

    x.join()
    y.join()

def M02(eve):
    # align to AN8
    # M02 Theater Change Cinema
    eve.aaasetup()    

    x = threading.Thread(target = eve.moveblock, args = (30,30,600,) )
    y = threading.Thread(target = eve.motor_mover, args = (40,1.25,eve.attach,))

    x.start()
    y.start()

    x.join()
    y.join()

    for x in range (2):
        eve.motor_mover(10,-1.1,eve.attach)
        eve.motor_mover(20,1.1,eve.attach)
    
    x = threading.Thread(target = eve.moveblock, args = (-50,-50,620,) )
    y = threading.Thread(target = eve.motor_mover, args = (40,-1.25,eve.attach,))

    x.start()
    y.start()

    x.join()
    y.join()

def M03(eve):
    # align to AE6 - use jig
    # M09 Movie Set
    
    eve.aaasetup()

    x = threading.Thread(target = eve.moveblock, args = (20,20,450))
    y = threading.Thread(target = eve.motor_mover, args = (50,1.5,eve.attach))

    x.start()
    y.start()

    x.join()
    y.join()

    eve.motor_mover(50,-1.5,eve.attach)
    eve.moveblock(-10,-10,105)
    eve.moveblock(-10,10,30)
    eve.motor_mover(50,3,eve.attach)
    eve.moveblock(-10,10,10)
    eve.moveblock(20,20,320)
    eve.moveblock(20,30,330)
    eve.moveblock(20,20,90)
    eve.motor_mover(20,-2.75,eve.attach)
    eve.motor_mover(40,2.75,eve.attach)
    
    
    x = threading.Thread(target = eve.moveblock, args = (20,-20,55))
    y = threading.Thread(target = eve.motor_mover, args = (40,-3,eve.attach))

    x.start()
    y.start()

    x.join()
    y.join()
    
    eve.moveblock(20,20,360)
    eve.moveblock(70,-70,170)
    eve.moveblock(-10,-10,200)

    eve.moveblock(20,40,315)
    eve.moveblock(30,30,340)
    eve.moveblock(30,20,300)
    eve.moveblock(50,50,440)

def M04(eve):
    # align to BN7
    # Museum, Hologram Performer, and Expert Delivery
    eve.aaasetup()
    eve.moveblock(30,30,330,brake=False)
    #eve.aaasetup()
    eve.moveblock(27,40,500,brake=False)
    #eve.aaasetup()
    eve.moveblock(40,40,300,brake=False)
    eve.moveblock(40,27,140)
    #eve.aaasetup()
    eve.moveblock(-40,-35,200)
    eve.moveblock(-10,10,57)
    eve.moveblock(-40,-40,500)
    eve.moveblock(-10,10,120)
    eve.moveblock(50,50,590)
    
def M05(eve):
    #aim for mission model
    # M03 craft creator
    eve.aaasetup()
    eve.moveblock(30,30,370)
    eve.moveblock(-30,-30,370)

def M06(eve):
    # align to BN7
    # put 2 people in the music concert
    eve.aaasetup()
    eve.moveblock(30,30,330)
    eve.moveblock(27,40,125)
    eve.moveblock(30,30,370)
    eve.moveblock(-70,-70,790,brake=False)
    
    
def all_missions(eve):
    
    debug_print('About to run skatepark mission')
    M001(eve)

    debug_print('About to run theater change cinema')
    M02(eve)
    
    debug_print('About to run cinema')
    M00(eve)

    debug_print('About to run dragon mission')
    M01(eve)

    debug_print('About to run movie set missions')
    M03(eve)

    debug_print('BLUE BASE: About to run the craft creator mission - aim for it')
    M05(eve)

    debug_print('About to run Museum mission')
    M04(eve)

    debug_print('About to run Music Concert mission')
    M06(eve)

    

    