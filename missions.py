#!/usr/bin/env python3



#from ev3dev2.button import Button
#from ev3dev2.sound import Sound
#from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import MoveTank, LineFollowErrorTooFast, follow_for_forever
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, SpeedPercent, follow_for_ms
#from ev3dev2.wheel import Wheel
#from ev3dev2.sensor import INPUT_1, INPUT_2,  INPUT_4
#from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor

from myblocks import  *
#from myblocks import follow_for_distance
#import logging as log

import os
import sys
import time
import threading




def mission_Step_Counter(eve):
    eve.aaasetup()
    eve.calibrategs()
    eve.moveblock(15,15,50)
    #eve.aaasetup()
    eve.turnblock(5,95)
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
    for _ in range(15):
        eve.moveblock(10,10,-20)
        eve.moveblock(10,10,50)
    #for x in range (1):
      #  eve.moveblock(7,7,-20)
       # eve.moveblock(7,7,80)

    x = threading.Thread(target = eve.moveblock, args = (60,60,-1500,) )
    #eve.moveblock(60,60,-1360)
    y = threading.Thread(target = eve.motor_mover, args = (50,-2,eve.turret,))
    
    x.start()
    y.start()
    #z.start()

    x.join()
    y.join()
    #z.join()  


def calibrate(eve):
    eve.calibrategs()
    eve.calibratecs(10,2)


def mission_Row_Machine(eve):
    #eve.calibrategs()
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
    eve.moveblock(0,15,1053)
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
    eve.turnblock(5,73)
    #eve.aaasetup()
    eve.moveblock(50,50,-1875)
   
def mission_bench(eve):
    eve.aaasetup()
    time.sleep(0.5)
    eve.calibrategs()

    #eve.aaasetup()
    #Write suedo code here
    # move forward 340 mm while lowrring attatchment 1.5

    eve.moveblock(15,15,320)
    eve.motor_mover(50,-2.75,eve.attach)
    eve.turnblock(8,10)
    #eve.aaasetup()
    eve.moveblock(15,15,50)
    time.sleep(.5)
    #eve.aaasetup()
    eve.motor_mover(50,2.75,eve.attach)
    #eve.aaasetup()
    time.sleep(0.25)

    
    y = threading.Thread(target = eve.motor_mover, args = (75,-3.75,eve.attach,))
    z = threading.Thread(target = eve.motor_mover, args = (20,2,eve.turret,))

    y.start()
    z.start()

    y.join()
    z.join()
    
    #eve.aaasetup()
     #Move the attachment back to it's original positon 
    x = threading.Thread(target = eve.moveblock,args = (35,30,-365,))
    y = threading.Thread(target = eve.motor_mover, args = (75,3.75,eve.attach,))
    z = threading.Thread(target = eve.motor_mover, args = (25,-2,eve.turret,))

    x.start()
    y.start()
    z.start()

    x.join()
    y.join()
    z.join()


def allmissions(eve):
    mission_Row_Machine(eve)
    mission_Step_Counter(eve)
    mission_bench(eve)
    

def mission_basket(eve):
    eve.aaasetup()  
    eve.calibrategs()

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

    #eve.turnblock(10,-30)
    eve.motor_mover(50,-2.5,eve.attach)
    time.sleep(0.5)
    #eve.aaasetup()
    eve.moveblock(10,10,60,brake=False)
    time.sleep(0.25)

    #eve.aaasetup()
    eve.motor_mover(75,1.75,eve.attach)
    time.sleep(0.25)
    eve.moveblock(20,20,-50,brake=False)
    eve.motor_mover(50,.75,eve.attach)

    #slide
    eve.turnblock(10,95)
    eve.moveblock(10,10,85)
    eve.line_finder(10,10,'r','b')
    #turn more if the attachment doesn't push man down
    eve.turnblock(10,40)
    eve.motor_mover(50,.5,eve.attach)
    #eve.motor_mover(25,-3,eve.turret)
    
    #eve.aaasetup()
    eve.turnblock(10,-40)
    eve.motor_mover(50,-.5,eve.attach)
    #eve.aaasetup()
    #eve.line_finder(10,10,'r','b')
    
    try:
        eve.athfollow_line(
            #kp=2, ki=0.060, #kd=3,
            kp=2, ki=0.00, kd=0,         # use this for change of directions speed = 10       
            #kp=2, ki=0.000, #kd=0,           # use this for speed=20 on straight lines
            speed=SpeedPercent(15),
            cs_for_line = eve.csr,            
            follow_left_edge=False,
            sleep_time=0.002,
            follow_for=follow_until_line,cs_for_until = eve.csl, wb = 'b',tolerence=2
            #follow_for = follow_for_distance,distance = 425
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise

    try:
        eve.athfollow_line(
            #kp=2, ki=0.060, #kd=3,
            kp=2, ki=0.00, kd=0,         # use this for change of directions speed = 10       
            #kp=2, ki=0.000, #kd=0,           # use this for speed=20 on straight lines
            speed=SpeedPercent(15),
            cs_for_line = eve.csr,            
            follow_left_edge=False,
            sleep_time=0.002,
            follow_for=follow_until_line,cs_for_until = eve.csl, wb = 'b',tolerence=2
            #follow_for = follow_for_distance,distance = 425
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise

    eve.aaasetup()



 
