#!/usr/bin/python

import time
import os


def GoodNight():
    # send color temperature down
    os.system("irsend SEND_START light.lircd.conf KEY_DOWN; sleep 3")
    time.sleep(1)
    os.system("irsend SEND_STOP light.lircd.conf KEY_DOWN")

    # send brightness down
    os.system("irsend SEND_START light.lircd.conf KEY_BRIGHTNESSDOWN; sleep 3")
    time.sleep(1)
    os.system("irsend SEND_STOP light.lircd.conf KEY_BRIGHTNESSDOWN")

    # send the night mode
    os.system("irsend SEND_ONCE light.lircd.conf KEY_N")

GoodNight()

