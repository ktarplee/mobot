import RPi.GPIO as GPIO
import time
import pi_servo_hat
import math

# setup sonar
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

test = pi_servo_hat.PiServoHat()
test.restart()

sonar = 5


def measure():
    GPIO.output(TRIG, False)
    time.sleep(0.2)

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


minTheta, maxTheta, step = -30, 130, 5


print("theta,distance")
for theta in list(range(minTheta, maxTheta, step)) + list(
    range(maxTheta, minTheta, -step)
):
    # move servo
    test.move_servo_position(sonar, theta)
    time.sleep(0.03)
    r = measure()
    x = r*math.cos(theta)
    y = r*math.sin(theta)

    # measure distance with sonar
    print(f"{theta},{r},{x},{y}")

