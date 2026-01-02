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

thetas = list(range(minTheta, maxTheta, step))
# thetas += list(range(maxTheta, minTheta, -step))

print("theta,distance,x,y")
for theta in thetas:
    # move servo
    servoHat.move_servo_position(sonar, theta)
    time.sleep(0.03)
    r = sensor.distance
    t = theta + 50
    x = r * math.cos(math.radians(t))
    y = r * math.sin(math.radians(t))

    # measure distance with sonar
    print(f"{t},{r},{x:.2f},{y:.1f}")
