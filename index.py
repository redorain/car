from bottle import get,post,run,request,template

import RPi.GPIO as GPIO
import time
import sys
import random
from run import *
from csb import *
reload(sys)
sys.setdefaultencoding('GB2312')

def main(status):


    if status == "front":
        forward(1)
#        stop(0.1)
    elif status == "leftFront":
        left(1)
#        stop(0.1)
    elif status == "rightFront":
        right(1)
#        stop(0.1)
    elif status == "rear":
        reverse(1)
#        stop(0.1)
    elif status == "leftRear":
        left_0(1)
#        stop(0.1)
    elif status == "rightRear":
        right_0(1)
#        stop(0.1)
    elif status == "stop":
        stop(0.1)

while True:
    distance = Measure()
    cnt = 0
    last = random.choice([0,1])
    while distance < 30 :        
        stop(0.1)
        if last == 0:
            left_0(0.20)            
        else:
            right_0(0.20)
        distance = Measure()
        if cnt > 6:
            break
        cnt += 1
    if cnt <= 6
        forwad(1)
    time.sleep(2)

def remember():
    


@get("/")
def index():
    return template("index")
@post("/cmd")
def cmd():
    adss=request.body.read().decode()
    print("press the button:"+adss)
    main(adss)
    return "OK"
run(host="0.0.0.0")

