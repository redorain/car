#!/usr/bin/python
#encoding:utf-8


import RPi.GPIO

time_out=5
Infrared=20

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(Infrared,RPi.GPIO.IN)

try:
    while True:
	    if(RPi.GPIO.input(Infrared)==True):
	    	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" Smoe is here !"
	    else:
	    	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" Nobody !"
	    time.sleep(time_out)
	    
except keyboardInterrupt:
    pass
RPi.GPIO.cleanup()

