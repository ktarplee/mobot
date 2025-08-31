import RPi.GPIO as GPIO
import time
import smbus

# setup
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

bus = smbus.SMBus(1)
addr = 0x40

bus.write_byte_data(addr, 0, 0x20) # enable the chip
time.sleep(.1)
bus.write_byte_data(addr, 0, 0x10) # enable Prescale change as noted in the datasheet
time.sleep(.1) # delay for reset
bus.write_byte_data(addr, 0xfe, 0x79) # changes the Prescale register value for 50 Hz, using the equation in the datasheet
time.sleep(.1)
bus.write_byte_data(addr, 0, 0x20) # enables the chip
time.sleep(.1)

def scale(x, in_min, in_max, out_min, out_max):
	return round((x - in_min)*(out_max - out_min)/(in_max - in_min) + out_min)

bus.write_word_data(addr, 0x1a, 0) # ch 5 start time = 0us
bus.write_word_data(addr, 0x1c, 305) # ch 5 end time = 1.5ms

sonar = 0x1c # ch 5

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

while True:
  # setting = scale(270, 50, 250, 209, 416)
  # bus.write_word_data(addr, 0x1c, setting)
  # time.sleep(2)

  for theta in list(range(0,270,10)) + list(range(270,0,-10)):
    # move servo
    setting = scale(theta, 50, 250, 209, 416)
    bus.write_word_data(addr, 0x1c, setting) # ch 5

    time.sleep(0.03)
    
    # measure distance with sonar
    print(theta, measure())

