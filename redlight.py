#!/usr/bin/python
#encoding:utf-8

import RPi.GPIO as GPIO
import time

HC_SR501 = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(HC_SR501,GPIO.IN)

try:
    while True:
        if(GPIO.input(HC_SR501) == True):
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" someone is here ")
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" nobody ")
        time.sleep(1)
            
except:
    pass

GPIO.cleanup()

