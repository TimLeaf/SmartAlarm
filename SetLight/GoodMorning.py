#!/usr/bin/python

import time
import os


def GoodMorning():
    # open light
    os.system("irsend SEND_ONCE light.lircd.conf KEY_OPEN")

    for i in range(1, 10):
        if i % 2 == 0:
            # send color temperature up
            os.system("irsend SEND_START light.lircd.conf KEY_UP; sleepenh 0.3 > 0")
            os.system("irsend SEND_STOP light.lircd.conf KEY_UP")

        # send brightness up
        os.system("irsend SEND_START light.lircd.conf KEY_BRIGHTNESSUP; sleepenh 0.3 > 0")
        os.system("irsend SEND_STOP light.lircd.conf KEY_BRIGHTNESSUP")

        time.sleep(90)

GoodMorning()

