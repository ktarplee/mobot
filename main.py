#!/usr/bin/env python

import smbus
import time

bus = smbus.SMBus(1)
addr = 0x40

def scale(x, in_min, in_max, out_min, out_max):
	return round((x - in_min)*(out_max - out_min)/(in_max - in_min) + out_min)

right = 0x12
left = 0x16

def setup():
    ## enable the PCA9685 and enable autoincrement
    bus.write_byte_data(addr, 0, 0x20)
    bus.write_byte_data(addr, 0xfe, 0x1e)

    # channel 0
    bus.write_word_data(addr, 0x06, 0)
    bus.write_word_data(addr, 0x08, 1250)

    # channel 1
    bus.write_word_data(addr, 0x0a, 0)
    bus.write_word_data(addr, 0x0c, 1250)

    # channel 3
    bus.write_word_data(addr, 0x12, 0)
    bus.write_word_data(addr, 0x14, 1250)

    # channel 4
    bus.write_word_data(addr, 0x16, 0)
    bus.write_word_data(addr, 0x18, 1250)



def scaleMotor(x):
    return scale(x, -100, 100, 125, 1750)

def move(leftSpeed, rightSpeed):
    l = scale(leftSpeed, -100, 100, 125, 1750)
    r = scale(rightSpeed, -100, 100, 125, 1750)
    print(l, r)
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

if __name__ == "__main__":
    setup()
    # pan_setting = scale(int(line_array[1]), 80, 220, 833, 1667)
    # tilt_setting = scale(int(line_array[2]), 50, 250, 833, 1667)
    # bus.write_word_data(addr, 0x08, pan_setting)
    # bus.write_word_data(addr, 0x0c, tilt_setting)

