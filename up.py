import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) #����GPIO������ģʽ

IN1 = 7   #���øղŽ��ߵ�GPIO��
IN2 = 11
IN3 = 13
IN4 = 15
GPIO.setup(IN1,GPIO.OUT)  #����GPIO��Ϊ���ģʽ
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

GPIO.output(IN1,GPIO.HIGH)  #����L298N�Ĳ���˵�����ı��ƽ
GPIO.output(IN2,GPIO.LOW)
GPIO.output(IN3,GPIO.LOW)
GPIO.output(IN4,GPIO.HIGH)
