#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, SpeedRPM, follow_for_ms
from ev3dev2.motor import Motor, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.led import Leds
from ev3dev2.wheel import Wheel
from ev3dev2.sound import Sound
from ev3dev2.button import Button

from math import pi

# Write your program here
mysound = Sound()
mysound.beep()


class MCTire(Wheel):
    """
    part number 56145
    comes in set 31313
    """
    def __init__(self):
        Wheel.__init__(self, 100.3, 17)



def initmotors():

    lw = Motor(OUTPUT_C)
    rw = Motor(OUTPUT_B)

    for x in (lw,rw):
        x.polarity = 'inversed'
        x.ramp_up_sp = 2000
        x.ramp_down_sp = 2000



    global mtank
    global WhDia   
    global WhDis 

    WhDia = 100.3  
    WhDis = 129.3

    mtank = MoveTank(OUTPUT_C, OUTPUT_B)

    mtank.gyro = GyroSensor()

    mtank.set_polarity('inversed')
 


    


def mission1(speed, angle, distance):

    rotations = WhDia * pi / distance
    mtank.on_for_rotations(SpeedPercent(speed),SpeedPercent(speed),rotations)


def main():
    initmotors()

    mission1(30,0,200)

if __name__ == '__main__':
    main()

