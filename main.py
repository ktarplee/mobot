#!/usr/bin/env python

import pi_servo_hat
import sys
import tty
import termios

# servos are connected as follows
# ch 0 is arm pan
# ch 1 is arm tilt
# ch 2 is arm grab
# ch 3 is drive left
# ch 4 is drive right
# ch 5 is sonar pan

servoHat = pi_servo_hat.PiServoHat()
servoHat.restart()


def scale(x, in_min, in_max, out_min, out_max):
    return round((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


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


right = 3
left = 4

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
    return scale(x, -100, 100, 202, 409)


# move is the workhorse of motion.  You can pass -100 to 100 for full reverse or full forward on either left or right.
def move(leftSpeed, rightSpeed):
    leftValue = scaleMotor(-leftSpeed)
    rightValue = scaleMotor(rightSpeed)
    print("LR", leftValue, rightValue)
    servoHat.move_servo_position(left, leftValue)
    servoHat.move_servo_position(right, rightValue)


def stop():
    move(0, 0)


def forward(speed):
    move(speed, speed)


def reverse(speed):
    move(-speed, -speed)


def rightTurn(speed):
    move(speed, 0)


def leftTurn(speed):
    move(0, speed)


def gimbal(pan, tilt, grab):
    # print("PT", pan, tilt)
    servoHat.move_servo_position(0, pan)
    servoHat.move_servo_position(1, tilt)
    servoHat.move_servo_position(2, grab)


if __name__ == "__main__":
    print('Control the mobot with the "uiok" keys.')
    print('Control the pan/tilt with "werd" keys.')
    print("Space bar to stop")
    print("q to quit.")

    pan = 120  # pan is backwords
    tilt = 90  # tilt is backwords
    grab = 45  # neutral grab
    speed = 100  # [0, 100]

    while True:
        ch = getch()
        if not ch:
            print("Done")
        # print("read string", ch, "with length", len(ch))

        # locomotion control
        if ch == " ":
            stop()
        elif ch == "i":
            forward(speed)
        elif ch == "k":
            reverse(speed)
        elif ch == "u":
            leftTurn(speed)
        elif ch == "o":
            rightTurn(speed)

        # pan/tilt control
        elif ch == "w":
            pan += 10
        elif ch == "e":
            tilt -= 10
        elif ch == "r":
            pan -= 10
        elif ch == "d":
            tilt += 10

        elif ch == "s":
            grab += 10
        elif ch == "f":
            grab -= 10

        elif ch == "n":
            speed -= 10
            speed = max(0, speed)
            print("speed", speed)
        elif ch == "m":
            speed += 10
            speed = min(100, speed)
            print("speed", speed)

        elif ch == "q":
            print("Quitting")
            break
        # else:
        #     stop()

        gimbal(pan, tilt, grab)
    stop()
