#!/usr/bin/env python3


from time import sleep
from ev3dev2.sound import Sound

from ev3dev2.motor import MoveTank, MoveSteering, SpeedPercent
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import SpeedNativeUnits, follow_for_forever, LineFollowErrorLostLine, LineFollowErrorTooFast
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM


from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
import math 
import time

from logging import getLogger

log = getLogger(__name__)

class AthMoveTank(MoveTank):
    def __init__(self, left_motor_port, right_motor_port,
            Wheel_Dia,
            csl , csr, # left and right color sensor
            desc=None, motor_class=LargeMotor):

        MoveTank.__init__(self, left_motor_port, right_motor_port, desc, motor_class)
        self.wheel_Dia = Wheel_Dia
        self.Circumference = Wheel_Dia * math.pi

        # create and set atrributes for sensors
        self.csl = ColorSensor(csl)
        self.csr = ColorSensor(csr)
  
        self.csl.mode = 'COL-REFLECT'
        self.csr.mode = 'COL-REFLECT'        
        
        self.csl_min = 0
        self.csl_max = 100
        self.csl_mid = 50
        self.csr_min = 0
        self.csr_max = 100
        self.csr_mid = 50

    def calibratecs(self,speed=20, time=5):
        self.csl_min = 0
        self.csl_max = 100
        self.csr_min = 0
        self.csr_max = 100

        # dont start until button is pushed!!

        end_time = time.time() + time
        
        MoveTank.on(self,speed,speed)
        while time.time() < end_time:
            readl = self.csl.value()
            readr = self.csr.value()
            if self.csl_max < readl:
                self.csl_max = readl
            if self.csl_min > readl:
                self.csl_min = readl
            if self.csr_max < readr:
                self.csr_max = readr
            if self.csr_min > readr:
                self.csr_min = readr
 
        MoveTank.off(self)

        self.csl_mid = (self.csl_max - self.csl_min) / 2
        self.csr_mid = (self.csr_max - self.csr_min) / 2


    def moveblock(self, speed, distance, brake=True, block=True):

        rotations = distance / self.Circumference
        MoveTank.on_for_rotations(speed,speed, rotations, brake, block)


    def turnblock(self, speed, target_angle, brake=True, error_margin=2, sleep_time=0.01):
 
        MoveTank.turn_degrees(speed,target_angle,brake, error_margin, sleep_time)


    def athfollow_line(self,
            kp, ki, kd,
            speed,
            cs_for_line,
            cs_for_follow,                             
            target_light_intensity=None,
            follow_left_edge=True,
            white=60,
            off_line_count_max=20,
            sleep_time=0.01,
            follow_for=follow_for_forever,
            **kwargs
        ):
        """
        PID line follower

        ``kp``, ``ki``, and ``kd`` are the PID constants.

        ``speed`` is the desired speed of the midpoint of the robot

        ``target_light_intensity`` is the reflected light intensity when the color sensor
            is on the edge of the line.  If this is None we assume that the color sensor
            is on the edge of the line and will take a reading to set this variable.

        ``follow_left_edge`` determines if we follow the left or right edge of the line

        ``white`` is the reflected_light_intensity that is used to determine if we have
            lost the line

        ``off_line_count_max`` is how many consecutive times through the loop the
            reflected_light_intensity must be greater than ``white`` before we
            declare the line lost and raise an exception

        ``sleep_time`` is how many seconds we sleep on each pass through
            the loop.  This is to give the robot a chance to react
            to the new motor settings. This should be something small such
            as 0.01 (10ms).

        ``follow_for`` is called to determine if we should keep following the
            line or stop.  This function will be passed ``self`` (the current
            ``MoveTank`` object). Current supported options are:
            - ``follow_for_forever``
            - ``follow_for_ms``

        ``**kwargs`` will be passed to the ``follow_for`` function

        Example:

        .. code:: python

            from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent, follow_for_ms
            from ev3dev2.sensor.lego import ColorSensor

            tank = MoveTank(OUTPUT_A, OUTPUT_B)
            tank.cs = ColorSensor()

            try:
                # Follow the line for 4500ms
                tank.follow_line(
                    kp=11.3, ki=0.05, kd=3.2,
                    speed=SpeedPercent(30),
                    follow_for=follow_for_ms,
                    ms=4500
                )
            except Exception:
                tank.stop()
                raise
        """
        self.cs = cs_for_line #set the input color sensor to tank
        assert self._cs, "ColorSensor must be defined"

        if target_light_intensity is None:
            target_light_intensity = self._cs.reflected_light_intensity

        integral = 0.0
        last_error = 0.0
        derivative = 0.0
        off_line_count = 0
        speed_native_units = speed.to_native_units(self.left_motor)
        MAX_SPEED = SpeedNativeUnits(self.max_speed)

        while follow_for(self, **kwargs):
            reflected_light_intensity = self._cs.reflected_light_intensity
            error = target_light_intensity - reflected_light_intensity
            integral = integral + error
            derivative = error - last_error
            last_error = error
            turn_native_units = (kp * error) + (ki * integral) + (kd * derivative)

            if not follow_left_edge:
                turn_native_units *= -1

            left_speed = SpeedNativeUnits(speed_native_units - turn_native_units)
            right_speed = SpeedNativeUnits(speed_native_units + turn_native_units)

            if left_speed > MAX_SPEED:
                log.info("%s: left_speed %s is greater than MAX_SPEED %s"  % (self, left_speed, MAX_SPEED))
                self.stop()
                raise LineFollowErrorTooFast("The robot is moving too fast to follow the line")

            if right_speed > MAX_SPEED:
                log.info("%s: right_speed %s is greater than MAX_SPEED %s"  % (self, right_speed, MAX_SPEED))
                self.stop()
                raise LineFollowErrorTooFast("The robot is moving too fast to follow the line")

            # Have we lost the line?
            if reflected_light_intensity >= white:
                off_line_count += 1

                if off_line_count >= off_line_count_max:
                    self.stop()
                    raise LineFollowErrorLostLine("we lost the line")
            else:
                off_line_count = 0

            if sleep_time:
                time.sleep(sleep_time)

            self.on(left_speed, right_speed)

        self.stop()