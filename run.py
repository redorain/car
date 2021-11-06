# -*- coding: utf-8 -*-


import time
import RPi.GPIO
from csb import *
from redlight2 import *

GPIO.setmode(GPIO.BCM)
IN1_PIN1 = 19
IN2_PIN1 = 16
IN1_PIN2 = 26
IN2_PIN2 = 20
GPIO.setwarnings(False)
GPIO.setup(IN1_PIN1, GPIO.OUT)
p1 = GPIO.PWM(IN1_PIN1, 35)  # 这里的50是频率为50Hz
p1.start(0)

GPIO.setup(IN2_PIN1, GPIO.OUT) 
p2 = GPIO.PWM(IN2_PIN1, 35)
p2.start(0)

GPIO.setup(IN1_PIN2, GPIO.OUT) 
p3 = GPIO.PWM(IN1_PIN2, 35)
p3.start(0)

GPIO.setup(IN2_PIN2, GPIO.OUT) 
p4 = GPIO.PWM(IN2_PIN2, 35)
p4.start(0)
rot = 35

# 可以通过更改括号内的数值改变电机转动的速度，数值范围0~100
def forward(time_sleep):
    p1.start(rot)
    p2.start(0)
    p3.start(rot)
    p4.start(0)
    time.sleep(time_sleep)


def reverse(time_sleep):
    p1.start(0)
    p2.start(rot)
    p3.start(0)
    p4.start(rot)
    time.sleep(time_sleep)


def left(time_sleep):
    p1.start(rot)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    time.sleep(time_sleep)


def right(time_sleep):
    p1.start(0)
    p2.start(0)
    p3.start(rot)
    p4.start(0)
    time.sleep(time_sleep)


def left_0(time_sleep):
    p1.start(rot)
    p2.start(0)
    p3.start(0)
    p4.start(rot)
    time.sleep(time_sleep)


def right_0(time_sleep):
    p1.start(0)
    p2.start(rot)
    p3.start(rot)
    p4.start(0)
    time.sleep(time_sleep)


def stop(time_sleep):
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    time.sleep(time_sleep)

def avoid():
    distance = Measure()
    cnt = 0
    last = random.choice([0,1])
    while distance < 30 or RPi.GPIO.input(5)==True:
        stop(0.1)
        if last == 0:
            left_0(0.20)
            stop(0.1)
        else:
            right_0(0.20)
            stop(0.1)
        distance = Measure()
        if cnt > 6:
            break
        cnt += 1
    if cnt <= 6:
        forward(1)
        stop(0.1)
    time.sleep(2)

def fly():
    for i in range(0, 5):
        forward(1)
        stop(0.1)
#        avoid()
    left(1)
    stop(0.1)
 #   avoid()
    for i in range(0, 3):
        forward(1)
        stop(0.1)
#        avoid()
    left(1)
    stop(0.1)
#    avoid()
    for i in range(0, 5):
        forward(1)
        stop(0.1)
#        avoid()
    right(1)
    stop(0.1)
#    avoid()
    for i in range(0, 3):
        forward(1)
        stop(0.1)
#        avoid()
    right(1)
    stop(0.1)
#    avoid()


def run_rem():
    global press
    for i in range(0, str(press)):
        if press[i] == "front":
            front(1)
        elif press[i] == "leftFront":
            left(1)
        elif press[i] == "rightFront":
            right(1)
        elif press[i] == "rear":
            reverse(1)
        elif press[i] == "leftRear":
            left_0(1)
        elif press[i] == "rightRear":
            right_0(1)
        elif press[i] == "stop":
            stop(1)
    press = []


def clc_rem():
    global press
    press = []
'''
while True:
    cmd = str(input("按以下键后回车（w，前进;s，后退;x，停止）:"))
    direction = cmd
    if direction == "w" or "s" or "a" or "d" or "q" or "e":
        if direction == "w":  # 前进
            forward(1)
            stop(0.1)
        elif direction == "s":  # 后退
            reverse(1)
            stop(0.1)
        elif direction == "a":  # 单轮左转
            left(1)
            stop(0.1)
        elif direction == "d":  # 单轮右转
            right(1)
            stop(0.1)
        elif direction == "q":  # 双轮左转
            left_0(1)
            stop(0.1)
        elif direction == "e":  # 双轮右转
            right_0(1)
            stop(0.1)

        elif direction == "x":  # 停止移动
            stop(0.1)
        else:
            print("命令无法识别")
            break
'''
