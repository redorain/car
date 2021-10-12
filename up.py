import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) #设置GPIO口引用模式

IN1 = 7   #引用刚才接线的GPIO口
IN2 = 11
IN3 = 13
IN4 = 15
GPIO.setup(IN1,GPIO.OUT)  #设置GPIO口为输出模式
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

GPIO.output(IN1,GPIO.HIGH)  #根据L298N的操作说明来改变电平
GPIO.output(IN2,GPIO.LOW)
GPIO.output(IN3,GPIO.LOW)
GPIO.output(IN4,GPIO.HIGH)
