#!/usr/bin/env python3
import LCD1602
import time

def setup():
	LCD1602.init(0x27,1) #LCD Address and Background Color

def exit():
	LCD1602.clear()

def start():
	welcome_string='Clock Hour'
	LCD1602.write(0,0,welcome_string)
	while(True):
		LCD1602.write(1,1,str(int(time.time()*1000)))
		time.sleep(.05)

if __name__ == '__main__':
	setup()
	try:
		start()
	except KeyboardInterrupt:
		print('User Interrupted')
		exit()


