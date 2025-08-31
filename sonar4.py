import RPi.GPIO as GPIO
import time
import pi_servo_hat

# setup
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

test = pi_servo_hat.PiServoHat()

test.restart()

sonar = 5

def measure():
  GPIO.output(TRIG, False)
  time.sleep(0.5)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
  
  # wait until ECHO goes high
  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  # wait until ECHO goes low
  while GPIO.input(ECHO)==1:
   pulse_end = time.time()

  # calculate distance
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  return distance

minTheta, maxTheta, step = -30, 130, 10

while True:
  for theta in list(range(minTheta, maxTheta, step)) + list(range(maxTheta, minTheta, -step)):
    # move servo
    test.move_servo_position(sonar, theta)
    time.sleep(0.03)
    
    # measure distance with sonar
    print(f'{theta}, {measure()}')

