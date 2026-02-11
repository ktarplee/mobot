import RPi.GPIO as GPIO
import time

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
GPIO.setup(BUTTON_CENTER, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Press buttons to test... (Ctrl+C to exit)")

try:
    while True:
        if GPIO.input(BUTTON_LEFT) == False:
            print("Button LEFT Pressed")
            time.sleep(0.2)
        if GPIO.input(BUTTON_RIGHT) == False:
            print("Button RIGHT Pressed")
            time.sleep(0.2)
        if GPIO.input(BUTTON_UP) == False:
            print("Button UP Pressed")
            time.sleep(0.2)
        if GPIO.input(BUTTON_DOWN) == False:
            print("Button DOWN Pressed")
            time.sleep(0.2)
        time.sleep(0.01)
        if GPIO.input(BUTTON_KEY1) == False:
            print("Button KEY1 Pressed")
            time.sleep(0.2)
        time.sleep(0.01)
        if GPIO.input(BUTTON_KEY2) == False:
            print("Button KEY2 Pressed")
            time.sleep(0.2)
        time.sleep(0.01)
        if GPIO.input(BUTTON_KEY3) == False:
            print("Button KEY3 Pressed")
            time.sleep(0.2)
        time.sleep(0.01)
        if GPIO.input(BUTTON_CENTER) == False:
            print("Button CENTER Pressed")
            time.sleep(0.2)
        time.sleep(0.01)

        
except KeyboardInterrupt:
    GPIO.cleanup()
