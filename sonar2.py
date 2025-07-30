import RPi.GPIO as GPIO
import time

# setup
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:
  time.sleep(1)

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
  print("Distance:",distance,"cm")

