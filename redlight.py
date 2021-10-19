#!/usr/bin/python
#encoding:utf-8

# Ŀǰ�õ�������⴫����ģ�����������͵ģ���˸�Ӧ�ľ���ֻ��һ��
# ����⵽����ʱ��������ߵ�ƽ2��4��

import RPi.GPIO as GPIO
import time

HC_SR501 = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(HC_SR501,GPIO.IN)

try:
    while True:
        if(GPIO.input(HC_SR501) == True):
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" ����!����һ�������� ")
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" ���������Χû��! ")
        time.sleep(1)
            
except:
    pass

GPIO.cleanup()

