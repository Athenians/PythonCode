#!/usr/bin/env python3


from ev3dev2.sound import Sound

from ev3dev2.motor import MoveTank
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, Motor
from ev3dev2.motor import follow_for_forever, LineFollowErrorLostLine, LineFollowErrorTooFast
from ev3dev2.motor import SpeedNativeUnits, SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM,speed_to_speedvalue


from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, GyroSensor
from ev3dev2.button import Button
import math 
import time
from globals import debug_print
from logging import getLogger

log = getLogger(__name__)

btn = Button()

class EveColorSensor(ColorSensor):
    def __init__(self,port):

        ColorSensor.__init__(self,port)

        self.min = 0
        self.mid = 0
        self.max = 0

class EveTank(MoveTank):
    def __init__(self, left_motor_port, right_motor_port,
            Wheel_Dia,
            csl_port , csr_port, # left and right color sensor
            gy_port,
            turret_port,
            attach_port,
            desc=None, motor_class=LargeMotor):
        """
        DB If eve = AthMoveTank(Output_B,Ouput_C, other parameters)
        eve. turret/attach. on would make the small motors turn on anD move since we created them into attributes in AthMoveTank
        """
        MoveTank.__init__(self, left_motor_port, right_motor_port, desc, motor_class)


        # set up robot
        self.set_polarity('inversed')
        self.ramp_up_sp = 2000
        self.ramp_down_sp = 2000

    
        #set up small motors
        self.turret = Motor(turret_port)
        self.attach = Motor(attach_port)

        #set up gyro sensor
        self.gyro = GyroSensor(gy_port)

        # create and set atrributes for sensors
        self.csl = EveColorSensor(csl_port)
        self.csr = EveColorSensor(csr_port)

        self.csl.mode = 'COL-REFLECT'
        self.csr.mode = 'COL-REFLECT'        
        #0=black
        #100 = white
        #50 = black and white
        #set up min, max, and mid for both color sensors
        #self.csl_min = 0
        #self.csl_max = 100
        #self.csl_mid = 50
        #self.csr_min = 0
        #self.csr_max = 100
        #self.csr_mid = 50

        self.csl.min = 0
        self.csl.max = 100
        self.csl.mid = 50
        self.csr.min = 0
        self.csr.max = 100
        self.csr.mid = 50

        # set up wheel data
        self.wheel_Dia = Wheel_Dia
        self.Circumference = Wheel_Dia * math.pi


    def calibrategs(self):
        debug_print('GS Calibration begin')
        for _ in range(2):
            self.gyro.mode = 'GYRO-RATE'
            self.gyro.mode = 'GYRO-ANG'
            time.sleep(.5)       
        gsnow = self.gyro.angle
        debug_print('GS Calibration finish ' + str(gsnow))

    def  calibratecs(self,speed=10, itime=4):
        self.csl.min = 100
        self.csl.max = 0
        self.csr.min = 100
        self.csr.max = 0

        # dont start until button is pushed!!

        end_time = time.time() + itime
    
        #DB Reads mins and maxs of both sensors and chages it based on what it read
        self.on(speed,speed)
        while time.time() < end_time:
            readl = self.csl.value()
            readr = self.csr.value()
            if self.csl.max < readl:
                self.csl.max = readl
            if self.csl.min > readl:
                self.csl.min = readl
            if self.csr.max < readr:
                self.csr.max = readr
            if self.csr.min > readr:
                self.csr.min = readr
            time.sleep(.01)  
        self.off()

        self.csl.mid = (self.csl.max - self.csl.min) / 2
        self.csr.mid = (self.csr.max - self.csr.min) / 2

        debug_print('left min: ' + str(self.csl.min) 
            + ' left mid: ' + str(self.csl.mid)
            + ' left max: ' + str(self.csl.max))
        debug_print('right min: ' + str(self.csr.min)
            + ' right mid: ' + str(self.csr.mid)
            + ' right max: ' + str(self.csr.max))

    #sets buttons so when called and pressed will do what was coded to do once pressed
    def left(self,state):
        if state:
            debug_print('Left button pressed')
            self.turret.on(speed=45)
        else:
            debug_print('Left button released')
            self.turret.off()
        return 0
    
    def right(self,state):  
        if state:
            debug_print('right button pressed')
            self.turret.on(speed=-45)
        else:
            debug_print('right button released')
            self.turret.off()

        return 0
    
    def up(self,state):
        if state:
            debug_print('Up button pressed')
            self.attach.on(speed=25)
        else:
            debug_print('Up button released')
            self.attach.off()
        return 0
    
    def down(self,state):
        if state:
            debug_print('Down button pressed')
            self.attach.on(speed=-25)
        else:
            debug_print('Down button released')
            self.attach.off()
        return 0

    def enter(self,state):
        if state:
            debug_print('Enter button pressed')
        else:
            debug_print('Enter button released')


    def aaasetup(self):

        debug_print('aaasetup begin')
        print('hit a button')  
        time.sleep(1)
        #DB TO press button you have to use btn.on and direction you want to move
        btn.on_left = self.left
        btn.on_right = self.right
        btn.on_up = self.up
        btn.on_down = self.down
        btn.on_enter = self.enter

        while True:
            #debug_print(btn.buttons_pressed)
            if btn.check_buttons(buttons=['enter']):
                debug_print('enter button hit')
                break
            btn.process()
            time.sleep(0.01)

        self.turret.reset
        self.attach.reset

        debug_print('aaasetup End')

    def moveblock(self, lspeed, rspeed, distance, brake=True, block=True):

        self.left_motor.reset
        self.right_motor.reset

        rotations = distance / self.Circumference

        #debug_print('moveblock lspeed = ' + str(lspeed))
        #debug_print('moveblock rspeed = ' + str(rspeed))
        #debug_print('moveblock distance = ' + str(distance))
        #debug_print('moveblock Circumference = ' + str(self.Circumference))
        #debug_print('moveblock rotations = ' + str(rotations))

        self.on_for_rotations(lspeed,rspeed,rotations)
        

    def turnblock(self, speed, target_angle, brake=True, error_margin=2, sleep_time=0.01):
        """
        turnblock
        """
        gsnow = self._gyro.angle
        debug_print('turnblock Start Angle ' + str(gsnow))

        self.turn_degrees(speed,target_angle,brake, error_margin, sleep_time)

        gsnow = self._gyro.angle
        debug_print('turnblock End Angle ' + str(gsnow))


<<<<<<< HEAD
    def line_finder(self,lspeed=10,rspeed=10,left_or_rightsensor='l', wb='w', tolerance=5):
        """     
        inputs:

        lspeed - speed for left wheel

        rspeed - speed for right wheel

        left_or_rightsensor - which sensor will find the line

        wb - find (w)hite or (b)lack

        tolerence - tolerence from min or max
        """

        if left_or_rightsensor == 'l':
            xmin = self.csl.min
            #xmid = self.csl_mid
            xmax = self.csl.max
            xsensor = self.csl
        else:
            xmin = self.csr.min
            #xmid = self.csr_mid
            xmax = self.csr.max
            xsensor = self.csr

        xmax -= tolerance
        xmin += tolerance

        while True:
            self.on(lspeed,rspeed)
            xread = xsensor.value()
            #debug_print('xread = ' + str(xread))           
            if wb == 'w' and xread >= xmax:
                break
            if wb == 'b' and xread <= xmin:
                break           
            time.sleep(0.01)

        self.off()



    def follow_for_distance(self, distance):
=======
    def follow_for_distance(self,speed,distance):
>>>>>>> folllow for distance
        #Pseudo Code
        #reset motor to 0 to start distance 
        #keep track of left and right motor distance average/location
        #follow line for inputed distance given
        #Once inputed distance is complete, stop 
        
        #reset left and right motor to 0 to start distance
        self.left_motor.position = 0
        self.right_motor.position = 0 
        reset = self.left_motor.position + self.right_motor.position
        #DB location  
       
        #For left motor
        left_pos = self.left_motor.position      # this gets you the current motor position of the left motor - returns encoder counts
        left_rotations = float(left_pos / self.left_motor.count_per_rot)  # this converts encoder counts to rotations
        left_mm = float(left_rotations * self.wheel_Dia)  # distance travelled on the LEFT wheel
        
        #for right motor
        right_pos = self.left_motor.position      # this gets you the current motor position of the left motor - returns encoder counts
        right_rotations = float(right_pos / self.left_motor.count_per_rot)  # this converts encoder counts to rotations
        right_mm = float(right_rotations * self.wheel_Dia)  # distance travelled on the LEFT wheel
        target_location = distance + reset
        
        #keeps track of location in mm 
        current_mm = (left_mm + right_mm) / 2

        #follow line for inputed distance given
        if current_mm != target_location:
            return True#follow line
       # else:
            #stopfollowing line 
         

        return True

    def follow_until_line(self,reflected_light_intensity,target_light_intensity):
        # pseudo code
        # DB enter 0 or 100 for what color to find to stop 
        # follow line
        # stops when while loop is false
        # and returns true at the end 
        #while (reflected_light_intensity != when_to_stop_enter_number ):
            #return True
            #else:
                #return False
        

        return True    


    def athfollow_line(self,
            kp, ki, kd,
            speed,
            cs_for_line,
            #cs_for_follow, this will be passed in **kwargs                            
            target_light_intensity=None,
            follow_left_edge=True,
            white=60,
            off_line_count_max=20,
            sleep_time=0.01,
            follow_for = follow_for_forever,
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

        white = self.cs.max

        target_light_intensity = self.cs.mid   
        #if target_light_intensity is None:
           # target_light_intensity = self._cs.reflected_light_intensity

        debug_print('white = ' + str(white) + '  tli = ' + str(target_light_intensity))

        integral = 0.0
        last_error = 0.0
        derivative = 0.0
        off_line_count = 0
        speed = speed_to_speedvalue(speed)
        speed_native_units = speed.to_native_units(self.left_motor)

        #MAX_SPEED = SpeedNativeUnits(self.max_speed)

        start_time = time.time() 

        while follow_for(self, **kwargs):
            reflected_light_intensity = self._cs.reflected_light_intensity
            error = target_light_intensity - reflected_light_intensity
            integral = integral + error
            derivative = error - last_error
            last_error = error
            turn_native_units = (kp * error) + (ki * integral) + (kd * derivative)

            if not follow_left_edge:
                turn_native_units *= -1
            
            debug_print(
                  'Timer: ' + str(time.time() - start_time)
                + ' kp: ' + str(kp)
                + ' ki: ' + str(ki)
                + ' kd: ' + str(kd)
                + ' rli: ' + str(reflected_light_intensity) 
                + ' error: ' + str(error) 
                + ' integral: ' + str(integral)
                + ' derivative: ' + str(derivative)
                + ' turn_native_units: ' + str(turn_native_units))

            left_speed = SpeedNativeUnits(speed_native_units - turn_native_units)
            right_speed = SpeedNativeUnits(speed_native_units + turn_native_units)

          #  if left_speed > MAX_SPEED:
          #      log.info("%s: left_speed %s is greater than MAX_SPEED %s"  % (self, left_speed, MAX_SPEED))
          #      self.stop()
          #      raise LineFollowErrorTooFast("The robot is moving too fast to follow the line")

          #  if right_speed > MAX_SPEED:
          #      log.info("%s: right_speed %s is greater than MAX_SPEED %s"  % (self, right_speed, MAX_SPEED))
          #      self.stop()
          #      raise LineFollowErrorTooFast("The robot is moving too fast to follow the line")

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
    
