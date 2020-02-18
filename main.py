#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from math import pi

# Write your program here
brick.sound.beep()


def initmotors():
    lw = motor(Port.C)    
    Rw = motor(Port.B)

    Wheel_Diameter = 100.3
    Wheel_Axle = 129.3

    lw.Direction = COUNTERCLOCKWISE
    rw.Direction = COUNTERCLOCKWISE

    robot = DriveBase(lw, rw, Wheel_Diameter, Wheel_Axle)

 def move(speed, distance,turn):

     lw.reset_angle(0)
     rw.reset_angle(0)

     distrot = distance * pi / Wheel_Diameter

     robot.drive(distrot,turn)

    if turn <= 0:
        while rw.angle() <= distrot:
            pass
    Else:
        while lw.angle() <= distrot:
            pass
    robot.Stop(stop.BRAKE)







def main():
    initmotors()

    robot



if __name__ == '__main__':
    main()

