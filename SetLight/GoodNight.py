#!/usr/bin/python

import subprocess


def subprocess_cmd(command):
    devnull = open('/dev/null', 'w')
    process = subprocess.Popen(command, stdout=devnull, stderr=devnull, shell=True)
    process.communicate()[0]


def GoodNight():
    # send color temperature down
    # os.system("irsend SEND_START light.lircd.conf KEY_DOWN; sleep 3")
    subprocess_cmd("irsend SEND_START light.lircd.conf KEY_DOWN; sleep 3")
    # os.system("irsend SEND_STOP light.lircd.conf KEY_DOWN")
    subprocess_cmd("irsend SEND_STOP light.lircd.conf KEY_DOWN")

    # send brightness down
    # os.system("irsend SEND_START light.lircd.conf KEY_BRIGHTNESSDOWN; sleep 3")
    subprocess_cmd("irsend SEND_START light.lircd.conf KEY_BRIGHTNESSDOWN; sleep 3")
    # os.system("irsend SEND_STOP light.lircd.conf KEY_BRIGHTNESSDOWN")
    subprocess_cmd("irsend SEND_STOP light.lircd.conf KEY_BRIGHTNESSDOWN")

    # send the night mode
    # os.system("irsend SEND_ONCE light.lircd.conf KEY_N")
    subprocess_cmd("irsend SEND_ONCE light.lircd.conf KEY_N")

GoodNight()
