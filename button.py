import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while(1):
	if GPIO.input(11) == 0:
		print("Button Pushed")
		sleep(1)

GPIO.cleanup()

