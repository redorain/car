from bottle import get, post, run, request, template


import RPi.GPIO as GPIO
import time
import sys
import random
from run import *
from csb import *
from yuyin import *

sys.setdefaultencoding('utf-8')

state = 3
now = 0
yuyin = 0
press = []


def main(status):
    global yuyin
    global now
    global press
    if status == "yuyin":
        if yuyin == 0:
            #os.system('espeak -vzh "%s"' % "on")
            print("open")
            yuyin = 1
        else:
            #os.system('espeak -vzh "%s"' % "off")
            print("close")
            yuyin = 0
    elif status == "fly":
        fly()
        now = 1
    elif status == "remember":
        now = 2
    elif status == "control":
        now = 3
    elif status == "run_rem":
        run_rem()
    elif status == "clc_rem":
        clc_rem()
    elif status() == "green":
        os.system('vlc --audio green.m4a')
    elif status() == "chushi":
        os.system('vlc --audio chushi.m4a')
    elif status == "front":
        if now == 3:
            forward(1)
            stop(0.1)
        if now == 2:
            press.append(status)
#        stop(0.1)
    elif status == "leftFront":
        if now == 3:
            left(1)
            stop(0.1)
        if now == 2:
            press.append(status)
    #        stop(0.1)
    elif status == "rightFront":
        if now == 3:
            right(1)
            stop(0.1)
        if now == 2:
            press.append(status)
    #        stop(0.1)
    elif status == "rear":
        if now == 3:
            reverse(1)
            stop(0.1)
        if now == 2:
            press.append(status)
    #        stop(0.1)
    elif status == "leftRear":
        if now == 3:
            left_0(1)
            stop(0.1)
        if now == 2:
            press.append(status)
    #        stop(0.1)
    elif status == "rightRear":
        if now == 3:
            right_0(1)
            stop(0.1)
        if now == 2:
            press.append(status)
    #        stop(0.1)
    elif status == "stop":
        if now == 3:
            stop(1)
        if now == 2:
            press.append(status)


@get("/")
def index():
    return template("index")


@post("/cmd")
def cmd():
    global yuyin
    adss = request.body.read().decode()
    print("press the button:" + adss)
    main(adss)
    while yuyin == 1:
        yuyinwork()
        adss = request.body.read().decode()
        if adss == "yuyin":
            yuyin = 0
            os.system('espeak -vzh "%s"' % "off")
    return "OK"


run(host="0.0.0.0")
