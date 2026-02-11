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
        draw.text((30, 40), text, fill="red")
    time.sleep(1)

# set GPIO pins according to your specific HAT (e.g. Pimoroni)
try:
    while True:
        # Wait until KEY1 is pressed
        wait_for_key()
        # Display Calvin
        display_text("Hello Calvin")

        # Wait until KEY1 is pressed
        wait_for_key()
        # Display Kyle
        display_text("Hello Kyle")

        # Wait until KEY1 is pressed
        wait_for_key()
        # Display Monica
        display_text("Hello Monica")

        # Wait until KEY1 is pressed
        wait_for_key()
        # Display Sadie
        display_text("Hello Sadie")

        # Wait until KEY1 is pressed
        wait_for_key()
        # Display Lydia 
        display_text("Hello Lydia")

        # Wait until KEY1 is pressed
        wait_for_key()
        # Display Tessa
        display_text("Hello Tessa")

        # Wait until KEY1 is pressed
        wait_for_key()
        # Display Katy 
        display_text("Hello Katy")

        # Wait until KEY1 is pressed
        wait_for_key()
        # Display Ruby
        display_text("Hello Ruby")

        # Wait until KEY1 is pressed
        wait_for_key()
        # Display Eliza
        display_text("Hello Eliza")

except KeyboardInterrupt:       
    GPIO.cleanup


