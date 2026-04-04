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

def display_text(text):
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="black", fill="white")
        draw.text((30,40), text, font=font, fill="blue")
    time.sleep(1)

x, y = (60, 55)
# set GPIO pins according to your specific HAT (e.g. Pimoroni)
try:
    while True:
        #on start display a box on screan then when you move the joysick up the box will move up and when the joystick moves down the box moves down and so on.

        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="black", fill="white")
            draw.text((x, y), "X", fill="blue")
        time.sleep(0.1)

        while True:
            if GPIO.input(BUTTON_CENTER) == False and x == 50 and y == 45:
                with canvas(device) as draw:
                    draw.rectangle([0, 115, 0 + 115, + height], outline="black", fill="white")
                    draw.text((x + 5, y + 5), "Hello", fill="blue")

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


