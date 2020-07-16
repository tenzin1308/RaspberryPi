import RPi.GPIO as gpio
import LCD1602 as lcd
from datetime import datetime
from time import sleep

def setup():
	lcd.init(0x27,1)
	gpio.setmode(gpio.BOARD)
	gpio.setup(btn,gpio.IN,pull_up_down=gpio.PUD_UP)
	gpio.setup(buzz,gpio.OUT)
	gpio.output(buzz,status)


def clock():
	lcd.write(0,0,str(datetime.now().strftime('%H:%M:%S:%f')))


def time():
	print('''
Enter the time to set the alarm in the format (hh:mm:ss)
Use 24hr clock
Example for 8:00 am = 8:00:00
	for 6:30 pm = 18:30:30''')
	return input()

def buzzer():
	global status
	global alarm_time
	if str(datetime.now().strftime('%H:%M:%S')) == alarm_time:
		status = not status
		lcd.write(1,1,'Alarm On ')
		gpio.output(buzz,status)

	if gpio.input(btn) == False:
		if status:
			status = not status
		else:
			status = not status
		if status:
			lcd.write(1,1,'Alarm Off')
		else:
			lcd.write(1,1,'Alarm On ')

		gpio.output(buzz,status)


def exit():
	lcd.clear()
	gpio.cleanup()

btn = 11
buzz =12
status  = True
alarm_time = ''

if __name__ == '__main__':
	try:
		setup()
		alarm_time = time()
		print('Alarm Started')
		while(True):
			clock()
			buzzer()

	except KeyboardInterrupt:
		print('User Terminated')
		exit()

	except:
		print('Found some error')
		exit()
