# coding:utf-8

import os
import time
import yuyinhecheng
import Turling
import yuyinshibie

tok = yuyinshibie.get_access_token()

switch = True
while switch:
    os.system('sudo arecord -D "plughw:2" -f S16_LE -r 16000 -d 3 /home/pi/Desktop/voice.wav')
    time.sleep(0.5)
    info = yuyinshibie.asr_main("/home/pi/Desktop/voice.wav", tok)
    if '关闭'.encode("utf-8") in info:
        while True:
            os.system('sudo arecord -D "plughw:1" -f S16_LE -r 16000 -d 10 /home/pi/Desktop/voice.wav')
            time.sleep(10)

            info = yuyinshibie.asr_main("/home/pi/Desktop/voice.wav", tok)
            if '开启'.encode("utf-8") in info:
                break

        url = "开启"
        os.system('espeak -vzh "%s"' % url)

    elif '暂停'.encode("utf-8") in info:
        url = "暂停"
        os.system('espeak -vzh"%s"' % url)
        time.sleep(10)

        url = "结束"
        os.system('espeak -vzh "%s"' % url)
        continue
    else:
        tex = Turling.Tuling(info)
        url = yuyinhecheng.yuyinhecheng_api(tok, tex)
        os.system('espeak -vzh "%s"' % tex)
        time.sleep(0.5)