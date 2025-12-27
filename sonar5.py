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


polar: list[str] = []
cartesian: list[str] = []
for theta in list(range(minTheta, maxTheta, step)):
    # move servo
    test.move_servo_position(sonar, theta)
    time.sleep(0.03)
    r = measure()
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    polar += f"{theta},{r}"
    cartesian += f"{x},{y}"

print("""
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
""")

print(f'''<svg height="200", width="300", xmlns="http://www.w3.org/2000/svg">
    <polyline points="{" ".join(polar)}" style="fill:none;stroke:green;stroke-width:3"/>
</svg>
''')

print(f'''<svg height="200", width="300", xmlns="http://www.w3.org/2000/svg">
    <polyline points="{" ".join(cartesian)}" style="fill:none;stroke:blue;stroke-width:3"/>
</svg>
''')

print("""
</body>
</html>
""")
