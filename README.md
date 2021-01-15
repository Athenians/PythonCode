# PythonCode

This code is the property of team Athenians.  It's use is limited to the team.  However, in the spirit of coopertition, other teams may view the code, and add comments via submitting issues.

Highlights
- All of our tank parameters are in a class called EveTank
	- funtions
		- calibrategs -- We calibrate our gyro sensor before each 
		- calibratecs -- We calibrate our color sensors by rolling forward slowly and measuring max and min values, and save the results in a pickle file so we don't have to calibrate each time we run a mission.
		- aaasetup -- this is used to position the attachments before each run.  We also use this to pause missions to determine where we are when debugging.
		- moveblock -- performs necessary calculations to perform on_for_rotations function to move a certain distance.
		- turnblock   -- performs a gyro turn
		- motor_mover -- generic motor control to use for any motor.
		- line_finder -- we roll the robot forward to find either white or black with either sensor
		- athfollow_line -- we can follow a line on either side of the line, and with either sensor using a PID controller.
			- follow_for_distance -- follows the line until a certain distance is reached
			- follow_until_line -- follows a line until the other sensor finds a line
- Menuing -- It was necessary to develop our own menu system because Python is slow to load.  we use the up/down buttons to select a function, left/right buttons move up a menu level, and the center button performs the function.  We organized the menu in the following way:
	- MAIN Menu
		- Doit -- runs all of our missions in one program
		- Tools
		- Missions
	- Tools
		- aaasetup --  Reposition the attachments while debugging.
		- CalibrateCS -- Run the color sensor calibration if needed
	- Missions
		- Step Counter -- performs the step counter mission
		- Row Machine -- performs the row mission and treadmill
		- Bench -- performs the bench mission
		- Basket -- performs the boccia (either red or blue), slide and dance


Thank you!
Signed -- Team Athenians
