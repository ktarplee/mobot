import time
import RPi.GPIO as GPIO

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7735
from PIL import Image, ImageDraw, ImageFont

serial = spi(port=0, device=0, gpio_DC=25, gpio_RST=27)
device = st7735(serial, width=128, height=128)

# Set GPIO pins according to your specific HAT (e.g., Pimoroni)
BUTTON_LEFT = 5
BUTTON_RIGHT = 26
BUTTON_DOWN = 19
BUTTON_UP = 6
BUTTON_CENTER = 13
BUTTON_KEY1 = 21
BUTTON_KEY2 = 20
BUTTON_KEY3 = 16

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_CENTER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_KEY1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_KEY2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_KEY3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font = ImageFont.truetype(font_path, 32)

x, y = (60, 55)

image = Image.new(device.mode, device.size)
draw = ImageDraw.Draw(image)
try:
    while True:
        draw.text((x, y), ".", fill="blue")
        device.display(image)
        time.sleep(0.1)
 
        while True:
            if GPIO.input(BUTTON_UP) == False:
                y -= 1
                break
            if GPIO.input(BUTTON_DOWN) ==False:
                y += 1
                break

            if GPIO.input(BUTTON_LEFT) == False:
                x -= 1
                break
            if GPIO.input(BUTTON_RIGHT) == False:
                x += 1
                break
            if GPIO.input(BUTTON_CENTER) == False:
                draw.text((x,y), "X", fill="red")
                break		

        x = min(max(x, 0), 128)
        y = min(max(y, 0), 128)
        print("post", x, y)

except KeyboardInterrupt:       
    GPIO.cleanup()


