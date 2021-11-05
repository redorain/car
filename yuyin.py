# coding:utf-8

import os
import time
import yuyinhecheng
import Turling
import yuyinshibie

tok = yuyinshibie.get_access_token()

switch = True

def yuyinwork():
        os.system('sudo arecord -D "plughw:1" -f S16_LE -r 16000 -d 10 /home/pi/Desktop/voice.wav')
        time.sleep(10)
        info = yuyinshibie.asr_main("/home/pi/Desktop/voice.wav", tok)        
        tex = Turling.Tuling(info)
        url = yuyinhecheng.yuyinhecheng_api(tok, tex)
        os.system('espeak -vzh "%s"' % tex)
        time.sleep(0.5)

'''
while switch:
    os.system('sudo arecord -D "plughw:2" -f S16_LE -r 16000 -d 3 /home/pi/Desktop/voice.wav')
    time.sleep(0.5)
    info = yuyinshibie.asr_main("/home/pi/Desktop/voice.wav", tok)
    if '¹Ø±Õ'.encode("utf-8") in info:
        while True:
            os.system('sudo arecord -D "plughw:1" -f S16_LE -r 16000 -d 10 /home/pi/Desktop/voice.wav')
            time.sleep(10)

            info = yuyinshibie.asr_main("/home/pi/Desktop/voice.wav", tok)
            if '¿ªÆô'.encode("utf-8") in info:
                break

        url = "¿ªÆô"
        os.system('espeak -vzh "%s"' % url)

    elif 'ÔÝÍ£'.encode("utf-8") in info:
        url = "ÔÝÍ£"
        os.system('espeak -vzh"%s"' % url)
        time.sleep(10)

        url = "½áÊø"
        os.system('espeak -vzh "%s"' % url)
        continue
    else:
        tex = Turling.Tuling(info)
        url = yuyinhecheng.yuyinhecheng_api(tok, tex)
        os.system('espeak -vzh "%s"' % tex)
        time.sleep(0.5)
'''