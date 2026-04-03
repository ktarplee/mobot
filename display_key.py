import time
import RPi.GPIO as GPIO

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.lcd.device import st7735

serial = spi(port=0, device=0, gpio_DC=25, gpio_RST=27)
device = st7735(serial, width=128, height=128)


# set GPIO pins according to your specific HAT (e.g. Pimoroni)
BUTTON_KEY1 = 21

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_KEY1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def wait_for_key():
    while True:
        if GPIO.input(BUTTON_KEY1) == False:
            print("Button KEY1 Pressed")
            break
        time.sleep(0.01)

def display_text(text):
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="black", fill="white")
        draw.text((30,100), text, fill="blue")
    time.sleep(5)


# set GPIO pins according to your specific HAT (e.g. Pimoroni)
try:
        # Wait until KEY1 is pressed
        wait_for_key()
        # Display Eliza
        display_text("Hello Eliza")

 
except KeyboardInterrupt:       
    GPIO.cleanup()

