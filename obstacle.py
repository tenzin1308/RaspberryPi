import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while(True):
        if GPIO.input(13) == 0 :
            print('obstracle dectected')
            time.sleep(.3)

except KeyboardInterrupt:
    print('Stoped')
    GPIO.cleanup()
except :
    print('found some error')
    GPIO.cleanup()
