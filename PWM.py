import RPi.GPIO as GPIO
from time import sleep
from math import pow
GPIO.setmode(GPIO.BOARD)
red = 12
yellow = 11
btn1 = 13
btn2 = 15
GPIO.setup(btn1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)
pwmR=GPIO.PWM(red,100)
pwmY=GPIO.PWM(yellow,100)
feq = 2
pwmR.start(feq)
pwmY.start(feq)
try:
	while(1):
		if GPIO.input(btn1) == 0:
			feq = pow(feq,2)
			if feq >100:
				print("You have reached max frequency")
				feq = 100
			pwmR.ChangeDutyCycle(feq)
			sleep(.1)
			pwmY.ChangeDutyCycle(feq)
			sleep(.1)
			print("frequency = ",feq)
		if GPIO.input(btn2) == 0:
			feq = pow(feq,.5)
			if feq <= 2:
				print("You have reached min frequency")
				feq = 2
			pwmR.ChangeDutyCycle(feq)
			sleep(.1)
			pwmY.ChangeDutyCycle(feq)
			sleep(.1)
			print("frequency = ",feq)

except KeyboardInterrupt:
	print("Keyboard Interrupted by pressing CTRL + C")
	GPIO.cleanup()

except:
	print("Something went wrong")
	GPIO.cleanup()
