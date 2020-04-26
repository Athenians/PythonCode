#!/usr/bin/env python3



from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.wheel import Wheel
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor

import logging as log


import os
import sys
import time


from aaasetup import aaasetup
from globals import *