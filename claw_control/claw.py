# https://www.instructables.com/Servo-Motor-Control-With-Raspberry-Pi/
import RPi.GPIO as GPIO
from time import sleep
# quickly test inputs with command line
import sys
set_angle = int(sys.argv[1])

print("Set angle: ", set_angle)


GPIO.setwarnings(False)

# Input: angle -> the angle you want the servo to rotate to
# Function: Calculates the duty cycle and sets the servo to that angle
def SetPWM(angle):
    # sets an duty cycle approximately to 90 degrees
	duty = angle
	# turns on the pin for output
	GPIO.output(11, True)
	# changes the duty cycle to match what we calculated
	pwm.ChangeDutyCycle(duty)
    # waits 1 second so the servo has time to make the turn
	# sleep(1)
	# turns off the pin
	# GPIO.output(11, False)
	# changes the duty back to 0 so we aren't continuously sending inputs to the servo
	# pwm.ChangeDutyCycle(0)

# we need to name all of the pins, so set the naming mode 
# as this sets the names to board mode, which just names the pins 
# according to the numbers
GPIO.setmode(GPIO.BOARD)

# we need an output to send our PWM signal on
# NOTE: Pin 11 is the GPIO pin and it can be changed
GPIO.setup(11, GPIO.OUT)

# setup PWM at 400 Hz
# The freq is unique to the servo motor
pwm=GPIO.PWM(11, 400)

# start it with 0 duty cycle so it doesn't set any angles on startup
pwm.start(20)
print("moved to 0 degrees")

sleep(6)
try:
	# setting test angles
	# for i in range(1, 91, 10):
	# 	print("pwm %: ", i)
	# 	set_angle = i
	# 	SetPWM(set_angle)
	# 	sleep(5)
	# for i in range(91, 1, -10):
	# 	print("pwm %: ", i)
	# 	set_angle = i
	# 	SetPWM(set_angle)
	# 	sleep(5)

	# angle 0
	print("set angle to: 90 degrees")
	set_angle = 48
	SetPWM(set_angle)
	sleep(5)

	pwm.ChangeDutyCycle(20)
	sleep(5)

finally:
	pwm.stop()
	GPIO.cleanup()