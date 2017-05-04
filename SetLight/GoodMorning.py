#!/usr/bin/python

import time, os

def GoodMorning():
    # open light
    os.system("irsend SEND_ONCE light.lircd.conf KEY_OPEN")

    for i in range(1,100):
        # send color temperature up
        os.system("irsend SEND_ONCE light.lircd.conf KEY_UP")
        time.sleep(1)

        # send brightness up
        os.system("irsend SEND_ONCE light.lircd.conf KEY_BRIGHTNESSUP")
        time.sleep(1)
        os.system("irsend SEND_ONCE light.lircd.conf KEY_BRIGHTNESSUP")
        time.sleep(1)

GoodMorning()

