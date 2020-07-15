#!/usr/bin/env python3
import LCD1602 as lcd
from datetime import datetime
import time

def setup():
	lcd.init(0x27,1) #LCD Address and Background Color

def exit():
	lcd.clear()
	bye_msg = 'Shutting Down In'
	lcd.write(0,0,bye_msg)
	lcd.write(1,7,str(3))
	time.sleep(1)
	lcd.write(1,7,str(2))
	time.sleep(1)
	lcd.write(1,7,str(1))
	time.sleep(1)

	lcd.clear()

def start():
	welcome_string='Clock Hour'
	lcd.write(0,0,welcome_string)
	while(True):
		lcd.write(1,1,datetime.now().strftime('%H:%M:%S:%f'))
		time.sleep(.05)

if __name__ == '__main__':
	setup()
	try:
		start()
	except KeyboardInterrupt:
		print('User Interrupted')
		exit()


