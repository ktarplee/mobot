#!/usr/bin/env python

import pi_servo_hat
import sys
import tty
import termios
import time
import RPi.GPIO as GPIO

# servos are connected as follows
# ch 0 is arm pan
# ch 1 is arm tilt
# ch 2 is arm grab
# ch 3 is drive left
# ch 4 is drive right
# ch 5 is sonar pan
armPanCh = 0
armTiltCh = 1
armGrabCh = 2
driveLeftCh = 4
driveRightCh = 3
sonarCh = 5

servoHat = pi_servo_hat.PiServoHat()
servoHat.restart()

# setup sonar
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def measure():
    "Measure the distance with the sonar range finder."
    GPIO.output(TRIG, False)
    time.sleep(0.5)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # wait until ECHO goes high
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # wait until ECHO goes low
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # calculate distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance


minTheta, maxTheta, step = -30, 130, 10


def scale(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def getch():
    """Get a single character from stdin, Unix version"""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())  # Raw read
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


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
    return scale(x, -100, 100, 0, 90)


# move is the workhorse of motion.  You can pass -100 to 100 for full reverse or full forward on either left or right.
def move(leftSpeed, rightSpeed):
    print("move", leftSpeed, rightSpeed)
    leftValue = scaleMotor(-leftSpeed)
    rightValue = scaleMotor(rightSpeed)
    print("LR", leftValue, rightValue)
    servoHat.move_servo_position(driveLeftCh, leftValue)
    servoHat.move_servo_position(driveRightCh, rightValue)


def main():
    print('Control the mobot with the "uiok" keys and speed with "nm"')
    print('Control the pan/tilt with "werd" keys.')
    print('Control sonar with "gh" and measure with "b"')
    print("Space bar to stop")
    print('"q" to quit.')

    # state
    left = 0  # [-100, 100]
    right = 0  # [-100, 100]
    speed = 100  # [0, 100]
    pan = 30  # pan is backwords
    tilt = 0  # tilt is backwords
    grab = 45  # neutral grab
    sonar = 40  # [-30, 130]

    while True:
        ch = getch()
        if not ch:
            print("Done")
        # print("read string", ch, "with length", len(ch))

        # locomotion control
        if ch == " ":
            left, right = 0, 0
        elif ch == "i":
            left, right = 100, 100
        elif ch == "k":
            left, right = -100, -100
        elif ch == "u":
            left, right = 0, 100
        elif ch == "o":
            left, right = 100, 0

        # pan/tilt control
        elif ch == "w":
            pan += 10
        elif ch == "e":
            tilt += 10
        elif ch == "r":
            pan -= 10
        elif ch == "d":
            tilt -= 10

        # grab
        elif ch == "s":
            grab -= 10
        elif ch == "f":
            grab += 10

        # sonar
        elif ch == "g":
            sonar += 10
            sonar = min(130, sonar)
        elif ch == "h":
            sonar -= 10
            sonar = max(-30, sonar)
        elif ch == "b":
            print("Sonar range is", measure(), "cm")

        # speed control
        elif ch == "n":
            speed -= 10
            speed = max(0, speed)
        elif ch == "m":
            speed += 10
            speed = min(100, speed)

        # quit
        elif ch == "q":
            print("Quitting")
            break

        print(f"({speed}) : {pan},{tilt},{grab} : {sonar}")

        move(left / 100 * speed, right / 100 * speed)
        servoHat.move_servo_position(armPanCh, pan)
        servoHat.move_servo_position(armTiltCh, tilt)
        servoHat.move_servo_position(armGrabCh, grab)
        servoHat.move_servo_position(sonarCh, sonar)

    move(0, 0)
    servoHat.sleep()


if __name__ == "__main__":
    main()
