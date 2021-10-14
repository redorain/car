import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(7, GPIO.IN)

while True:
    
    if GPIO.input(7)==1:
        nowtime = time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
        print(nowtime)
        print("有人来了！")
        GPIO.output(13,GPIO.HIGH)
    else:        
        pass
    time.sleep(0.5)
    GPIO.output(13,GPIO.LOW)
    time.sleep(5)