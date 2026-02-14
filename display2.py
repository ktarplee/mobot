import time
import RPi.GPIO as GPIO

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7735
from PIL import ImageFont

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
GPIO.setup(BUTTON_KEY1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_KEY2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_KEY3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font = ImageFont.truetype(font_path, 32)

def wait_for_key():
    while True:
        if GPIO.input(BUTTON_KEY1) == False:
            print("Button KEY1 Pressed")
            break
        time.sleep(0.01)

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


