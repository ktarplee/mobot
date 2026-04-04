import time
import RPi.GPIO as GPIO

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
GPIO.setup(BUTTON_CENTER, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def wait_for_key():
    while True:
        if GPIO.input(BUTTON_KEY1) == False:
            print("Button KEY1 Pressed")
            break
        time.sleep(0.01)

