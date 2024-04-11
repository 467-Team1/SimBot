# https://www.instructables.com/Servo-Motor-Control-With-Raspberry-Pi/
import RPi.GPIO as GPIO
from time import sleep
# quickly test inputs with command line
import sys
set_angle = int(sys.argv[1])
# hz = int(sys.argv[2])

print("Set angle: ", set_angle)
# print("Set hz: ", hz)


GPIO.setwarnings(False)

# Input: angle -> the angle you want the servo to rotate to
# Function: Calculates the duty cycle and sets the servo to that angle
def SetAngle(angle):
	# sets a variable equal to our angle divided by 18 and 2 added
	duty = angle / 18 + 2
	# turns on the pin for output
	GPIO.output(11, True)
	# changes the duty cycle to match what we calculated
	pwm.ChangeDutyCycle(duty)
    # waits 1 second so the servo has time to make the turn
	sleep(1)
	# turns off the pin
	GPIO.output(11, False)
	# changes the duty back to 0 so we aren't continuously sending inputs to the servo
	pwm.ChangeDutyCycle(0)

# we need to name all of the pins, so set the naming mode 
# as this sets the names to board mode, which just names the pins 
# according to the numbers
GPIO.setmode(GPIO.BOARD)

# we need an output to send our PWM signal on
GPIO.setup(11, GPIO.OUT)

# setup PWM on pin #3 at 50Hz
pwm=GPIO.PWM(11, 50)

# start it with 0 duty cycle so it doesn't set any angles on startup
pwm.start(0)

sleep(1)
try:
	# setting test angles
	SetAngle(set_angle)

finally:
	pwm.stop()
	GPIO.cleanup()