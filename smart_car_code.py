import RPi.GPIO as GPIO
import LCD1602 as LCD
from time import sleep

buzz = 12
ir_obstacle = 13
btn = 11
srv = 16

def setup():
    GPIO.setmode(GPIO.BOARD)
    LCD.init(0x27,1)


def start():
    GPIO.setup(buzz,GPIO.OUT)
    GPIO.setup(ir_obstacle,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btn,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(srv,GPIO.OUT)
    GPIO.output(buzz,True)
    servo = GPIO.PWM(srv,50)
    servo.start(0)
    if GPIO.input(ir_obstacle) != 0:
        LCD.write(0,0,'Moving Forward')
        LCD.write(1,1,'            ') 
        servo.ChangeDutyCycle(14)
        sleep(.1)
        servo.ChangeDutyCycle(0)
    if GPIO.input(ir_obstacle) == 0:
        LCD.write(0,0,'Obstacle ahead')
        LCD.write(1,1,'Turning back')
        servo.ChangeDutyCycle(50)
        sleep(.1)
        servo.ChangeDutyCycle(0)


def loop():
    while(True):
        start()
    

if __name__ == '__main__':
    try:
        command = input('Press S to start the Smart Car: ')
        if command.upper() == 'S':
            setup()
            loop()
        else:
            exit()
    except KeyboardInterrupt:
        print('User Interrupted: (Pressed "Ctl + C") ')
        servo.stop()
        LCD.clear()
        GPIO.cleanup()
                  