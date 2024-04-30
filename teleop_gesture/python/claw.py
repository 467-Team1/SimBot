# https://www.instructables.com/Servo-Motor-Control-With-Raspberry-Pi/
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO_pin = 0
GPIO_pin = input("What is the GPIO Pin for the Claw?")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_pin, GPIO.OUT)
pwm=GPIO.PWM(GPIO_pin, 400)

# Open Claw
print("Opening Claw...")
pwm.start(20)
sleep(3)

# CLose Claw
print("Closing Claw...")
pwm.ChangeDutyCycle(40)

pwm.stop()
GPIO.cleanup()