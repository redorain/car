#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bottle import get,post,run,request,template
 
import RPi.GPIO as GPIO
import time
import sys 
from run.py import *

 
####  ����main������
def main(status):
    

    if status == "front":
        forward(1)
        stop(0.1)
    elif status == "leftFront":
        left(1)
        stop(0.1)
    elif status == "rightFront":
        right(1)
        stop(0.1)
    elif status == "rear":
        reverse(1)
        stop(0.1)
    elif status == "leftRear":
        left_0(1)
        stop(0.1)
    elif status == "rightRear":
        right_0(1)
        stop(0.1)
    elif status == "stop":
        stop(0.1)      
             
 
 
 
@get("/")
def index():
    return template("index")
@post("/cmd")
def cmd():
    adss=request.body.read().decode()
    print("�����˰�ť:"+adss)
    main(adss)
    return "OK"
run(host="0.0.0.0")