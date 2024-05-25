#!/usr/bin/env python

import smbus
import time
import sys, tty, termios

def getch():
    """Get a single character from stdin, Unix version"""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())          # Raw read
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

bus = smbus.SMBus(1)
addr = 0x40

def scale(x, in_min, in_max, out_min, out_max):
	return round((x - in_min)*(out_max - out_min)/(in_max - in_min) + out_min)

right = 0x14 # ch 3
left = 0x18 # ch 4

def setup_200hz():
    ## enable the PCA9685 and enable autoincrement
    bus.write_byte_data(addr, 0, 0x20)
    time.sleep(.1)
    bus.write_byte_data(addr, 0xfe, 0x1e)
    time.sleep(.1)

    # channel 0
    bus.write_word_data(addr, 0x06, 0)
    bus.write_word_data(addr, 0x08, 1250)

    # channel 1
    bus.write_word_data(addr, 0x0a, 0)
    bus.write_word_data(addr, 0x0c, 1250)

    # channel 3
    bus.write_word_data(addr, 0x12, 0) # ch 3 start time = 0ms
    bus.write_word_data(addr, 0x14, 1250) # ch 3 stop time = 1.5ms

    # channel 4
    bus.write_word_data(addr, 0x16, 0)
    bus.write_word_data(addr, 0x18, 1250)

def setup_50hz():
    bus.write_byte_data(addr, 0, 0x20) # enable the chip
    time.sleep(.1)
    bus.write_byte_data(addr, 0, 0x10) # enable Prescale change as noted in the datasheet
    time.sleep(.1) # delay for reset
    bus.write_byte_data(addr, 0xfe, 0x79) # changes the Prescale register value for 50 Hz, using the equation in the datasheet
    time.sleep(.1)
    bus.write_byte_data(addr, 0, 0x20) # enables the chip

    time.sleep(.1)

    # 209, 312, 416 (305 seems to stop it)
    bus.write_word_data(addr, 0x06, 0) # ch 0 start time = 0us
    bus.write_word_data(addr, 0x08, 312) # ch 0 end time = 1.5ms

    bus.write_word_data(addr, 0x0a, 0) # ch 1 start time = 0us
    bus.write_word_data(addr, 0x0c, 312) # ch 1 end time = 1.5ms

    bus.write_word_data(addr, 0x12, 0) # ch 3 start time = 0us
    bus.write_word_data(addr, 0x14, 305) # ch 3 end time = 1.5ms

    bus.write_word_data(addr, 0x16, 0) # ch 4 start time = 0us
    bus.write_word_data(addr, 0x18, 305) # ch 4 end time = 1.5ms

# while True:
# 	pipein = open("/var/www/html/FIFO_pipan", 'r')
# 	line = pipein.readline()
# 	line_array = line.split(' ')
# 	if line_array[0] == "servo":
# 		pan_setting = scale(int(line_array[1]), 80, 220, 209, 416)
# 		tilt_setting = scale(int(line_array[2]), 50, 250, 209, 416)
# 		bus.write_word_data(addr, 0x08, pan_setting)
# 		bus.write_word_data(addr, 0x0c, tilt_setting)
# pipein.close()



def scaleMotor(x):
    return scale(x, -100, 100, 202, 409) # 50 hz
    # return scale(x, -100, 100, 833, 1667) # 200 hz

# move is the workhorse of motion.  You can pass -100 to 100 for full reverse or full forward on either left or right.
def move(leftSpeed, rightSpeed):
    l = scaleMotor(-leftSpeed)
    r = scaleMotor(rightSpeed)
    # print(l, r)
    moveRaw(l, r)

def moveRaw(leftValue, rightValue):
    bus.write_word_data(addr, left, leftValue)
    bus.write_word_data(addr, right, rightValue)

def stop():
    move(0, 0)

def forward():
    move(100, 100)

def reverse():
    move(-100, -100)

def rightTurn():
    move(100, 0)

def leftTurn():
    move(0, 100)

def gimbal(pan, tilt):
    print("PT", pan, tilt)
    pan_setting = scale(pan, 80, 220, 209, 416)
    tilt_setting = scale(tilt, 50, 250, 209, 416)
    bus.write_word_data(addr, 0x08, pan_setting)
    bus.write_word_data(addr, 0x0c, tilt_setting)

setup_50hz()

if __name__ == "__main__":
    print("Control the mobot with the \"uiok\" keys.  q to quit.")
    pan = 120 # pan is backwords
    tilt = 90 # tilt is backwords
    while True:
        ch = getch()
        if not ch:
            print("Done")
        # print("read string", ch, "with length", len(ch))
        
        # locomotion control
        if ch == " ":
            stop()
        elif ch == "i":
            forward()
        elif ch == "k":
            reverse()
        elif ch == "u":
            leftTurn()
        elif ch == "o":
            rightTurn()
        
        # pan/tilt control
        elif ch == "w":
            pan += 10
        elif ch == "e":
            tilt -= 10
        elif ch == "r":
            pan -= 10
        elif ch == "d":
            tilt += 10

        elif ch == "q":
            print("Quitting")
            break
        # else:
        #     stop()

        gimbal(pan, tilt)
    stop()
