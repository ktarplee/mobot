#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import os

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7735
from PIL import ImageFont

from buttons import *

serial = spi(port=0, device=0, gpio_DC=25, gpio_RST=27)
device = st7735(serial, width=128, height=128)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font = ImageFont.truetype(font_path, 32)

x, y = (60, 55)
# set GPIO pins according to your specific HAT (e.g. Pimoroni)
try:
    while True:
        # draw
        with canvas(device) as draw:
            # background
            draw.rectangle(device.bounding_box, fill="white")
            # draw a box
            draw.rectangle([0, 115, 0 + 128, 115 + 15], fill="red")
            draw.rectangle([0, 0, 0 + 128, 0 + 6], fill="red")
            draw.rectangle([15, 115, 15 + 10, 115 + 10], fill="black")
            draw.text((x, y), "X", fill="blue")
        time.sleep(0.1)

        # handle buttons
        while True:
            if GPIO.input(BUTTON_CENTER) == False and x == 50 and y == 45:
                with canvas(device) as draw:
                    draw.rectangle(device.bounding_box, outline="black", fill="white")
                   #draw.text((x + 5, y + 5), "Hello", fill="blue")

            if GPIO.input(BUTTON_KEY3) == False:
                print("Running display.py...")
                os.system("uv run display_pixel.py")  # run the other script
                break

            if GPIO.input(BUTTON_UP) == False:
                print("Button UP Pressed")
                y -= 5
                break
            if GPIO.input(BUTTON_DOWN) ==False:
                print("Button DOWN Pressed")
                y += 5
                break

            if GPIO.input(BUTTON_LEFT) == False:
                print("Button LEFT Pressed")
                x -= 5
                break
            if GPIO.input(BUTTON_RIGHT) == False:
                print("Button RIGHT Pressed")
                x += 5
                break

        print("prior", x, y)
        x = min(max(x, 0), 128)
        y = min(max(y, 0), 128)
        print("post", x, y)

except KeyboardInterrupt:
    GPIO.cleanup()


