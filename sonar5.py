import time
import pi_servo_hat
import math
from gpiozero import DistanceSensor

# setup sonar sensor
sensor = DistanceSensor(echo=24, trigger=23)

servoHat = pi_servo_hat.PiServoHat()
servoHat.restart()

sonar = 5

minTheta, maxTheta, step = -30, 130, 5

polar: list[str] = []
cartesian: list[str] = []
for theta in range(minTheta, maxTheta, step):
    # move servo
    servoHat.move_servo_position(sonar, theta)
    time.sleep(0.03)
    r = sensor.distance
    t = theta + 50
    x = r * math.cos(math.radians(t))
    y = r * math.sin(math.radians(t))

    polar += f"{t},{r}"
    cartesian += f"{x},{y}"

print("""
<!DOCTYPE html>
<html>
<head>
<title>Mobot Sonar</title>
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
