#!/usr/bin/env python3



#from ev3dev2.button import Button
#from ev3dev2.sound import Sound
#from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import MoveTank, LineFollowErrorTooFast, follow_for_forever
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, SpeedPercent, follow_for_ms
#from ev3dev2.wheel import Wheel
#from ev3dev2.sensor import INPUT_1, INPUT_2,  INPUT_4
#from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.led import Leds
from myblocks import EveTank, follow_until_line,follow_for_distance

#import logging as log

import os
import sys
import time
import threading



def mission01(eve):
    eve.calibrategs()
    eve.moveblock(25,25,30)
    eve.turnblock(10,80)
    eve.moveblock(25,25,1650)
    eve.turnblock(10,-80)


def mission02(eve):

    eve.calibrategs()
    for _ in range(4):
        eve.moveblock(25,25,400)
        eve.turnblock(10,90,error_margin=0)

    #eve.moveblock(25,25,1500)


def mission_Step_Counter(eve):
    z = threading.Thread(target = eve.leds.animate_police_lights, args =('BLACK','ORANGE','LEFT','RIGHT', 0.01, 20,))
    z.start()
    #eve.calibrategs()
    eve.aaasetup()
    eve.moveblock(7,7,50)
    #eve.aaasetup()
    eve.turnblock(10,92)
    #eve.aaasetup()

    x = threading.Thread(target = eve.moveblock, args = (25,25,800,) )
    #eve.moveblock(25,25,800)

    y = threading.Thread(target = eve.motor_mover, args = (50,2,eve.turret,))
    #z = threading.Thread(target = eve.motor_mover, args = (25,-4,eve.attach,))

    x.start()
    y.start()
    #z.start()

    x.join()
    y.join()
    #z.join()

    eve.moveblock(7,7,60)
   # for x in range (1):
      # eve.moveblock(7,10,-10)
       #eve.moveblock(7,7,50)    
    for x in range(20):
        eve.moveblock(10,10,-20)
        eve.moveblock(10,10,50)
    #for x in range (1):
      #  eve.moveblock(7,7,-20)
       # eve.moveblock(7,7,80)

    x = threading.Thread(target = eve.moveblock, args = (60,60,-1360,) )
    #eve.moveblock(60,60,-1360)
    y = threading.Thread(target = eve.motor_mover, args = (50,-2,eve.turret,))
    
    x.start()
    y.start()
    #z.start()

    x.join()
    y.join()
    #color thread
    z.join()  


def calibrate(eve):
    eve.calibrategs()
    eve.calibratecs(10,2)


def mission_Row_Machine(eve):
    z = threading.Thread(target = eve.leds.animate_police_lights, args =('BLACK','RED','LEFT','RIGHT', 0.01, 45,))   
    #eve.calibrategs()
    z.start()
    #eve.calibratecs(10,2)
    eve.aaasetup()
    time.sleep(0.5)
    eve.calibrategs
    eve.moveblock(20,20,115,brake=False)
    eve.line_finder(10,10,'r','b')

    
    eve.left_motor.position = 0
    eve.right_motor.position = 0 
    try:
        eve.athfollow_line(
            #kp=2, ki=0.060, #kd=3,
            kp=3, ki=0.00, kd=0,         # use this for change of directions speed = 10       
            #kp=2, ki=0.000, #kd=0,           # use this for speed=20 on straight lines
            speed=SpeedPercent(10),
            cs_for_line = eve.csr,            
            follow_left_edge=True,
            sleep_time=0.002,
            #follow_for=follow_until_line,cs_for_until = eve.csl, wb = 'b',tolerence=2
            follow_for = follow_for_distance,distance = 1120
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise

    eve.line_finder(5,5,'l','b')


   #this is to complete treadmill
    #eve.aaasetup()
    eve.moveblock(10,10,220)
    #eve.aaasetup()
    
    eve.motor_mover(60,-3.85,eve.attach)
    eve.moveblock(0,10,1000)
    eve.motor_mover(60,3.85,eve.attach)
    #eve.aaasetup()
 
    eve.moveblock(-15,-15,400)

    
    eve.turnblock(5,-90)
    eve.moveblock(-15,-15,240)
    time.sleep(1)
    
    eve.line_finder(5,5,'l','b')
   # eve.aaasetup()
    eve.moveblock(15,0,190)
    
    eve.line_finder(5,5,'l','b')



    #this is to complete row machine
    eve.turnblock(5,-45)
    #eve.aaasetup()
    eve.moveblock(10,10,37)
    #eve.aaasetup()
    # 3 45
    eve.motor_mover(40,-4.4,eve.attach)
    eve.turnblock(5,-35)
    eve.motor_mover(40,4.4,eve.attach)
    #eve.aaasetup()
    eve.turnblock(15,73)
    #eve.aaasetup()
    eve.moveblock(50,50,-1600)
    z.join()
   
def mission_bench(eve):
    x = threading.Thread(target = eve.leds.animate_police_lights, args =('BLACK','AMBER', 'LEFT','RIGHT', 0.01, 20,))
    x.start()
    eve.calibrategs()
    eve.aaasetup()

    #eve.aaasetup()
    #Write suedo code here
    # move forward 340 mm while lowrring attatchment 1.5

    eve.moveblock(15,15,320)
    eve.motor_mover(50,-3,eve.attach)
    eve.turnblock(8,10)
    #eve.aaasetup()
    eve.moveblock(15,15,40)
    time.sleep(1)
    #eve.aaasetup()
    eve.motor_mover(50,2.5,eve.attach)
    #eve.aaasetup()
    time.sleep(0.25)

    
    y = threading.Thread(target = eve.motor_mover, args = (75,-2.7,eve.attach,))
    z = threading.Thread(target = eve.motor_mover, args = (25,2,eve.turret,))

    y.start()
    z.start()

    y.join()
    z.join()
    
    eve.aaasetup()
    x.join()
    #Move the attachment back to it's original positon 
    x = threading.Thread(target = eve.moveblock,args = (35,30,-365,))
    y = threading.Thread(target = eve.motor_mover, args = (75,3.2,eve.attach,))
    z = threading.Thread(target = eve.motor_mover, args = (25,-2,eve.turret,))

    x.start()
    y.start()
    z.start()

    x.join()
    y.join()
    z.join()



def mission_basket(eve):
    z = threading.Thread(target = eve.leds.animate_police_lights, args =('BLACK','YELLOW', 'LEFT', 'RIGHT', 0.01, 35,))
    z.start()
    eve.calibrategs()
    #eve.aaasetup()
    #eve.calibratecs(10,2)
    eve.aaasetup()
   # eve.moveblovk(20,20,510)
   # eve.turnblock(20,90)
    #eve.line_finder(10,10,'l','b')
    #eve.moveblock()

    eve.moveblock(20,20,250,brake=False)
    eve.turnblock(10,90)
    eve.line_finder(10,10,'r','b')

    eve.moveblock(0,10,40)

    eve.left_motor.position = 0
    eve.right_motor.position = 0 
    try:
        eve.athfollow_line(
            #kp=2, ki=0.060, #kd=3,
            kp=4, ki=0.06, kd=3,         # use this for change of directions speed = 10       
            #kp=2, ki=0.000, #kd=0,           # use this for speed=20 on straight lines
            speed=SpeedPercent(5),
            cs_for_line = eve.csr,            
            follow_left_edge=True,
            sleep_time=0.002,
            #follow_for=follow_until_line,cs_for_until = eve.csl, wb = 'b',tolerence=2
            follow_for = follow_for_distance,distance = 220
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise


    eve.left_motor.position = 0
    eve.right_motor.position = 0 
    try:
        eve.athfollow_line(
            #kp=2, ki=0.060, #kd=3,
            kp=2, ki=0.00, kd=0,         # use this for change of directions speed = 10       
            #kp=2, ki=0.000, #kd=0,           # use this for speed=20 on straight lines
            speed=SpeedPercent(15),
            cs_for_line = eve.csr,            
            follow_left_edge=True,
            sleep_time=0.002,
            #follow_for=follow_until_line,cs_for_until = eve.csl, wb = 'b',tolerence=2
            follow_for = follow_for_distance,distance = 170
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise


    try:
        eve.athfollow_line(
            #kp=2, ki=0.060, #kd=3,
            kp=3, ki=0.00, kd=0,         # use this for change of directions speed = 10       
            #kp=2, ki=0.000, #kd=0,           # use this for speed=20 on straight lines
            speed=SpeedPercent(15),
            cs_for_line = eve.csr,            
            follow_left_edge=True,
            sleep_time=0.002,
            follow_for=follow_until_line,cs_for_until = eve.csl, wb = 'b',tolerence=2
            #follow_for = follow_for_distance,distance = 430
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise

    eve.moveblock(20,20,20,brake=False)
    time.sleep(0.25)

    eve.turnblock(10,-30)
    eve.motor_mover(50,-3.25,eve.attach)
    time.sleep(0.25)
    
    eve.moveblock(20,20,60,brake=False)

    eve.aaasetup()
    eve.motor_mover(75,3.25,eve.attach)
 
    eve.aaasetup()
    
    #PUT THIS AT THE END OF THE PROGRAMMING FOR MISSION
    z.join()
 
