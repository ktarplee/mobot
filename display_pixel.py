#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import os
import subprocess
import sys

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7735

serial = spi(port=0, device=0, gpio_DC=25, gpio_RST=27)
device = st7735(serial, width=128, height=128)


# set GPIO pins according to your specific HAT (e.g. Pimoroni)
BUTTON_KEY1 = 21
BUTTON_KEY2 = 20
BUTTON_KEY3 = 16


# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_KEY1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_KEY2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_KEY3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="black", fill="magenta")
        draw.text((45, 32),"names" , fill="red")
        draw.text((45, 70),"moveX" , fill="red")

    time.sleep(1)


    while True:

        if GPIO.input(BUTTON_KEY1) == False:
            print("Running display.py...")
            subprocess.run([sys.executable, "display.py"])  # run the other script

        if GPIO.input(BUTTON_KEY2) == False:
            print("Running display2.py...")
            subprocess.run([sys.executable, "display2.py"])  # run the other script
            
        if GPIO.input(BUTTON_KEY3) == False:
            print("shutdown")
            subprocess.run(["sudo", "poweroff"])
        time.sleep(0.1)

except KeyboardInterrupt:       
    GPIO.cleanup()

