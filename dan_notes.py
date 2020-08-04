
#  these are my notes.

#   pseudo code:

#   Mission xx
#   Place robot in starting position (manually)
#   ensure arm is 0x0
#   Move forward 30mm -- speed normal
#   turn 90deg -- speed normal
#   find line -- speed normal
#   follow line for 300 mm -- speed normal -- left side of line , right sensor
#   turn -90 -- speed normal
#   move forward 50mm -- speed fast
#   arm to 20x0
#   arm to 20x20
#   complete mission
#   go home
#   while going home, arm to 0x0


# commands you'll need
# left_pos = self.left_motor.position      # this gets you the current motor position of the left motor - returns encoder counts
# left_rotations = float(left_pos / self.left_motor.count_per_rot)  # this converts encoder counts to rotations
# left_mm = float(left_rotations * self.Wheel_Dia)  # distance travelled on the LEFT wheel
# current_mm = (left_mm + right_mm) / 2


