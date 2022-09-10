#!/usr/bin/env python3


#from ev3dev2.button import Button
#from ev3dev2.sound import Sound
#from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
#from ev3dev2.motor import MoveTank, LineFollowErrorTooFast, follow_for_forever
#from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, SpeedPercent, follow_for_ms
#from ev3dev2.wheel import Wheel
#from ev3dev2.sensor import INPUT_1, INPUT_2,  INPUT_4
#from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
#from ev3dev2.led import Leds
#from myblocks import EveTank, follow_until_line,follow_for_distance

#import logging as log

#import os
#import sys
#import time
#import threading


'''
def allmissions(eve):
    mission_Row_Machine(eve)
    mission_Step_Counter(eve)
    mission_bench(eve)
    mission_basket(eve)    
'''

'''
def mission_Step_Counter(eve):
    #z = threading.Thread(target = eve.leds.animate_police_lights, args =('BLACK','ORANGE','LEFT','RIGHT', 0.01, 20,))
    #z.start()

    #eve.calibrategs()
    eve.aaasetup()
    eve.moveblock(15,15,50)
    #eve.aaasetup()
    eve.turnblock(10,92)
    #eve.aaasetup()

    x = threading.Thread(target = eve.moveblock, args = (30,30,800,) )
    #eve.moveblock(25,25,800)

    y = threading.Thread(target = eve.motor_mover, args = (50,2,eve.turret,))
    #z = threading.Thread(target = eve.motor_mover, args = (25,-4,eve.attach,))

    x.start()
    y.start()
    #z.start()

    x.join()
    y.join()
    #z.join()

    eve.moveblock(15,15,60)
   # for x in range (1):
      # eve.moveblock(7,10,-10)
       #eve.moveblock(7,7,50)    
    for x in range(18):
        eve.moveblock(15,15,-9)
        eve.moveblock(10,10,30)
    #for x in range (1):
      #  eve.moveblock(7,7,-20)
       # eve.moveblock(7,7,80)
    #eve.sound.play_file('fanfare_x.wav')
    x = threading.Thread(target = eve.moveblock, args = (65,65,-1360,) )
    #eve.moveblock(60,60,-1360)
    y = threading.Thread(target = eve.motor_mover, args = (50,-2,eve.turret,))
    
    x.start()
    y.start()
    #z.start()

    x.join()
    y.join()
    #z.join()  
'''
'''
def calibrate(eve):
    eve.calibrategs()
    eve.calibratecs(10,2)
'''
'''
def mission_Row_Machine(eve):
    #z = threading.Thread(target = eve.leds.animate_police_lights, args =('BLACK','RED','LEFT','RIGHT', 0.01, 45,)) 	
    #z.start()
	
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
            speed=SpeedPercent(12),
            cs_for_line = eve.csr,            
            follow_left_edge=True,
            sleep_time=0.002,
            #follow_for=follow_until_line,cs_for_until = eve.csl, wb = 'b',tolerence=2
            follow_for = follow_for_distance,distance = 1070
            #follow_for=follow_for_forever
            #follow_for=follow_for_ms,  ms=4500
        
        )
    except LineFollowErrorTooFast:
        eve.stop() 
        raise
    
    #eve.aaasetup()
    eve.line_finder(10,10,'l','b')


   #this is to complete treadmill
    #eve.aaasetup()
    eve.moveblock(10,10,220)
    #eve.aaasetup()
    
    eve.motor_mover(60,-0.77,eve.attach)
    eve.moveblock(0,10,1000)
    eve.motor_mover(60,0.77,eve.attach)
    #eve.aaasetup()
    #eve.sound.play_file('fanfare_x.wav')
    eve.moveblock(-15,-15,375)

    eve.turnblock(5,-100)
    eve.moveblock(-20,-20,260)
    time.sleep(1)
    
    eve.line_finder(10,10,'l','b')
   # eve.aaasetup()
    eve.moveblock(15,0,190)
    
    eve.line_finder(10,10,'l','b')



    #this is to complete row machine
    eve.turnblock(5,-45)
    #eve.aaasetup()
    eve.moveblock(10,10,37)
    #eve.aaasetup()
    # 3 45
    eve.motor_mover(40,-0.75,eve.attach)
    eve.turnblock(5,-35)
    eve.turnblock(5,2)
    eve.motor_mover(40,0.75,eve.attach)
    #eve.aaasetup()
    eve.turnblock(5,70)
    #eve.aaasetup()
    #eve.sound.play_file('fanfare_x.wav')
    eve.moveblock(45,45,-1600)
    #z.join()
'''
'''
def mission_bench(eve):
    eve.aaasetup()
    time.sleep(0.25)
    eve.calibrategs
    #x = threading.Thread(target = eve.leds.animate_police_lights, args =('BLACK','AMBER', 'LEFT','RIGHT', 0.01, 9.253,))
    #x.start()
    #eve.aaasetup()
    #Write suedo code here
    # move forward 340 mm while lowrring attatchment 1.5

    eve.moveblock(20,20,320)
    eve.motor_mover(8,-0.6,eve.attach)
    eve.turnblock(8,10)
    #eve.aaasetup()
    eve.moveblock(15,15,40)
    time.sleep(1)
    #eve.aaasetup()
    eve.motor_mover(8,0.6,eve.attach)
    #eve.aaasetup()
    time.sleep(0.25)

    
    y = threading.Thread(target = eve.motor_mover, args = (15,-.75,eve.attach,))
    z = threading.Thread(target = eve.motor_mover, args = (25,2,eve.turret,))

    y.start()
    z.start()

    y.join()
    z.join()
    #x.join()
    #eve.aaasetup()
     #Move the attachment back to it's original positon 
    #eve.sound.play_file('fanfare_x.wav')
    x = threading.Thread(target = eve.moveblock,args = (55,50,-365,))
    y = threading.Thread(target = eve.motor_mover, args = (15,.75,eve.attach,))
    z = threading.Thread(target = eve.motor_mover, args = (25,-2,eve.turret,))

    x.start()
    y.start()
    z.start()

    x.join()
    y.join()
    z.join()
'''
'''
def mission_basket(eve):
    eve.aaasetup()
    time.sleep(0.5)
    eve.calibrategs
   # eve.moveblovk(20,20,510)
   # eve.turnblock(20,90)
    #eve.line_finder(10,10,'l','b')
    #eve.moveblock()

    eve.moveblock(25,25,250,brake=False)
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

    #################
    eve.motor_mover(30,-0.4,eve.attach)
    time.sleep(0.25)
    #eve.aaasetup()
    eve.moveblock(10,10,60,brake=False)
    time.sleep(0.25)

    #eve.aaasetup()
    eve.motor_mover(15,0.275,eve.attach)
    time.sleep(0.25)
    eve.moveblock(20,20,-50,brake=False)
    #eve.sound.play_file('fanfare_x.wav')
    #eve.motor_mover(15,0.15,eve.attach)

    #slide
    eve.turnblock(10,95)
    eve.moveblock(10,10,85)
    #eve.line_finder(10,10,'r','b')
    #turn more if the attachment doesn't push man down
    #eve.aaasetup()
    eve.turnblock(10,113)
    #eve.sound.play_file('fanfare_x.wav')
    #eve.aaasetup()
    eve.motor_mover(15,.125,eve.attach)
    #eve.motor_mover(25,-3,eve.turret)
    
    #eve.aaasetup()
    #eve.turnblock(10,-75)
    #eve.motor_mover(50,-.1,eve.attach)
    #eve.aaasetup()
    #eve.line_finder(10,10,'r','b')
    eve.moveblock(45,33.53,-400.53)
    #Dance Floor Lights
    #x = threading.Thread(target = eve.leds.animate_rainbow, args = ())
    #y = threading.Thread(target = eve.sound.play_file, args=('sounds/fanfare3.wav',))
    #x.start()
    #y.start()
    #attachment dance code
    
   

    eve.moveblock(20,20,15)   
    for _ in range(14):
        x = threading.Thread(target = eve.motor_mover, args=(16,-.5,eve.attach,))
        y = threading.Thread(target = eve.motor_mover, args=(15,2.5,eve.turret,))
        z = threading.Thread(target = eve.turnblock, args=(10,-20,))
        x.start()
        y.start()
        z.start()
        x.join()
        y.join()
        z.join()
        x = threading.Thread(target = eve.motor_mover, args=(16,.5,eve.attach,))
        y = threading.Thread(target = eve.motor_mover, args=(15,-2.5,eve.turret,))
        z = threading.Thread(target = eve.turnblock, args=(5,20,))
        x.start()
        y.start()
        z.start()
        x.join()
        y.join()
        z.join()
        ####
        #eve.motor_mover(17,1.5,eve.turret)
        #eve.turnblock(15,20)
        #eve.motor_mover(8,-0.2,eve.attach)
        #eve.turnblock(15-20)
        #eve.motor_mover(18,-1.5,eve.turret)
        #eve.motor_mover(8,0.2,eve.attach)
    #x.join()
    #y.join()
    #eve.aaasetup()


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
            speed=SpeedPercent(10),
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
    eve.turnblock(15,113)
    #food package dropped during this
    eve.motor_mover(55,3.85,eve.turret)
    eve.motor_mover(25,0.97,eve.attach)
    eve.moveblock(20,20,390)
    eve.motor_mover(55,-3.85,eve.turret)
    eve.motor_mover(55,1.6,eve.turret)
    eve.moveblock(20,20,-460)
    eve.motor_mover(55,1.5,eve.turret)
    eve.motor_mover(25,0.2,eve.attach)
    eve.moveblock(20,20,485)
    eve.moveblock(20,20,-50)
    eve.motor_mover(25,-0.6,eve.attach)
    eve.motor_mover(55,-1.5,eve.turret)
    eve.turnblock(10,90)
    eve.moveblock(20,20,245)
    eve.turnblock(10,35)
    eve.motor_mover(25,0.30,eve.attach)
    eve.motor_mover(55,-1.0,eve.turret)
    eve.moveblock(20,20,490)
    eve.turnblock(10,100)
    eve.moveblock(20,20,157.5)
    eve.turnblock(10,20)
    eve.moveblock(20,20,75)
    eve.moveblock(20,20,-280)
    eve.turnblock(5,45)
    eve.moveblock(20,20,-150)
    eve.turnblock(5,-65)
    eve.moveblock(10,10,-84)
    eve.motor_mover(55,-0.6,eve.turret)
    eve.motor_mover(15,-0.9,eve.attach)

 
def mission_unload_cargo_plane(eve):
    eve.aaasetup()
    eve.motor_mover(55,1.68,eve.turret)
    eve.moveblock(20,20,614)
    eve.motor_mover(25,2.0,eve.attach)
    eve.motor_mover(25,-2.0,eve.attach)
    eve.motor_mover(55,-1.68,eve.turret)
    eve.moveblock(20,10,-80)
    eve.turnblock(10,90)
    eve.moveblock(30,30,-500)


def mission_cargo_circle(eve):
    eve.aaasetup()
    eve.moveblock(20,20,222.5)
    eve.turnblock(5,90)    
    eve.moveblock(20,20,1040)
    eve.moveblock(0,30,165)
    eve.moveblock(20,20,40)
    eve.motor_mover(15,1.0,eve.attach)
    eve.motor_mover(55,2.5,eve.turret)
    eve.moveblock(20,20,-170)
    eve.motor_mover(15,-1.0,eve.attach)
    eve.turnblock(15,82)
    eve.motor_mover(55,-2.5,eve.turret)
    eve.moveblock(20,20,-310)
    eve.moveblock(0,30,60)
    eve.moveblock(35,35,-1250)
    #################
 '''
 