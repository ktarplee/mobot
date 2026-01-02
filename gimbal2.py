#!/usr/bin/env python

import sys
import tty
import termios
from gpiozero import Servo

pan = Servo(12)
tilt = Servo(18)


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


def main():
    print('Control the pan/tilt with "werd" keys.')
    print("Space bar to stop")
    print('"q" to quit.')

    while True:
        ch = getch()
        if not ch:
            print("Done")
        # print("read string", ch, "with length", len(ch))

        # pan/tilt control
        elif ch == "w":
            pan.value = min(1.0, pan.value + 0.1)
        elif ch == "e":
            tilt.value = min(1.0, tilt.value + 0.1)
        elif ch == "r":
            pan.value = max(-1.0, pan.value - 0.1)
        elif ch == "d":
            tilt.value = max(-1.0, tilt.value - 0.1)

        # quit
        elif ch == "q":
            print("Quitting")
            break


if __name__ == "__main__":
    main()
