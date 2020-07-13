import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
PhotoResistor = 11
Buzzer = 12
Laser = 16
GPIO.setup(PhotoResistor,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Buzzer,GPIO.OUT)
GPIO.setup(Laser,GPIO.OUT)
GPIO.output(Buzzer,GPIO.HIGH)
GPIO.output(Laser,False)
try:
	while(True):
		if GPIO.input(PhotoResistor) == 1:
			GPIO.output(Buzzer,GPIO.LOW)
		else :
			GPIO.output(Buzzer,GPIO.HIGH)
	
except KeyboardInterrupt:
	GPIO.cleanup()
