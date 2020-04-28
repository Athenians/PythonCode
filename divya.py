n=int(5)
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col)
    print()

#Forms a square, moves front, makes another square, and goes back to initial ares
tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)


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

steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
# drive in a turn for 10 rotations of the outer motor
steer_pair.on_for_rotations(steering=-60, speed=25, rotations=10)
steer_pair.off()
