
n=int(5)
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col)
    print()
<<<<<<< HEAD

from ev3dev2.motor import OUTPUT_C, OUTPUT_B, MoveTank, MoveSteering, 
from ev3dev2.sensor.lego import TouchSensor
from time import sleep
#Forms a square, moves front, makes another square, and goes back to initial area
=======
from ev3dev2.motor import OUTPUT_C, OUTPUT_B, MoveTank, MoveSteering, SpeedPercent
from ev3dev2.sensor.lego import TouchSensor
from time import sleep
#Forms a square, moves front, makes another square, and goes back to initial ares
>>>>>>> Divya-update
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)


for x in range(4):
    tank_pair.on(left_speed=-35, right_speed=-35)
    sleep(1)
    tank_pair.on_for_degrees(10,-10,150+(x*6))
    sleep(1)
tank_pair.on(left_speed=-65, right_speed=-65)
sleep(1)

for x in range(4):
    tank_pair.on(left_speed=-35, right_speed=-35)
    sleep(1)
    tank_pair.on_for_degrees(10,-10,160+(x*5))
    sleep(1)
tank_pair.on(left_speed=65, right_speed=65)
sleep(1)
<<<<<<< HEAD
=======

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
# drive in a turn for 10 rotations of the outer motor
steer_pair.on_for_rotations(steering=-60, speed=25, rotations=10)
steer_pair.off()
>>>>>>> Divya-update
