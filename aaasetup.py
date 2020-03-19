#!/usr/bin/env python3

from ev3dev2.button import Button
from ev3dev2.motor import  Motor, OUTPUT_A, OUTPUT_D

import time

from globals import *

btn = Button()

turret = Motor(OUTPUT_A)
attach = Motor(OUTPUT_D)



def left(state):
    if state:
        debug_print('Left button pressed')
        turret.on(speed=45)
    else:
        debug_print('Left button released')
        turret.off()
    return 0
   
def right(state):  
    if state:
        debug_print('right button pressed')
        turret.on(speed=-45)
    else:
        debug_print('right button released')
        turret.off()

    return 0
 
def up(state):
    if state:
        debug_print('Up button pressed')
        attach.on(speed=25)
    else:
        debug_print('Up button released')
        attach.off()
    return 0
   
def down(state):
    if state:
        debug_print('Down button pressed')
        attach.on(speed=-25)
    else:
        debug_print('Down button released')
        attach.off()
    return 0

def enter(state):
    if state:
        debug_print('Enter button pressed')
    else:
        debug_print('Enter button released')


def aaasetup():

    

    debug_print('aaasetup')
    print('hit a button')  
    btn.on_left = left
    btn.on_right = right
    btn.on_up = up
    btn.on_down = down
    btn.on_enter = enter

    while True:
        #debug_print(btn.buttons_pressed)
        if btn.check_buttons(buttons=['enter']):
            debug_print('enter button hit')
            break
        btn.process()
        time.sleep(0.01)

    turret.reset
    attach.reset
