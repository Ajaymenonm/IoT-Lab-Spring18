# basic one time blink

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # to use Raspberry Pi board pin numbers
GPIO.setup(11, GPIO.OUT) # set up GPIO output channel
    
GPIO.output(11, GPIO.LOW) # set RPi board pin 11 low. Turn off LED.
time.sleep(1)
GPIO.output(11, GPIO.HIGH) # set RPi board pin 11 high. Turn on LED.
time.sleep(2)

#==================================================================================

# Use BCM

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # to use Raspberry Pi board pin numbers
GPIO.setup(17, GPIO.OUT) # set up GPIO output channel

print('LED OFF')    
GPIO.output(17, GPIO.LOW) # set RPi bcm pin 17 low. Turn off LED.
time.sleep(1)
print('LED ON')
GPIO.output(17, GPIO.HIGH) # set RPi bcm pin 17 high. Turn on LED.
time.sleep(2)

#==================================================================================

# Infinite Loop

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # to use Raspberry Pi board pin numbers
GPIO.setup(17, GPIO.OUT) # set up GPIO output channel

while True:    
    GPIO.output(17, False) # set RPi board pin 11 low. Turn off LED.
    time.sleep(1)
    GPIO.output(17, True) # set RPi board pin 11 high. Turn on LED.
    time.sleep(2)

#==================================================================================

# Clean Up

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # to use Raspberry Pi board pin numbers
GPIO.setup(17, GPIO.OUT) # set up GPIO output channel
print('Hit Ctrl + C to exit')

try:
    while True:    
        GPIO.output(17, False) # set RPi board pin 11 low. Turn off LED.
        time.sleep(1)
        GPIO.output(17, True) # set RPi board pin 11 high. Turn on LED.
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()


#==================================================================================

# PWM

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(17,GPIO.OUT)     # initialize GPIO19 as an output.
p = GPIO.PWM(17,100)        # 100Hz frequency
p.start(0)                  #start at 0% duty cycle

while True:
    for x in range (50):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
 
    for x in range (50):
        p.ChangeDutyCycle(50-x)
        time.sleep(0.1)

#================================================================================

# Multiple LED's
import RPi.GPIO as GPIO
import time

pins = [11, 12, 13, 15]
GPIO.setmode(GPIO.BOARD)        # to use Raspberry Pi board pin numbers
  
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)   # Set all pins mode as output
    #GPIO.output(pin, GPIO.HIGH) # Set all pins to high(+3.3V)

def setup():
  try:
    loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()

def loop():
  while True:
    for pin in pins:
      GPIO.output(pin, GPIO.LOW)  
      time.sleep(0.05)
      GPIO.output(pin, GPIO.HIGH)
    for pin in reversed(pins):
      GPIO.output(pin, GPIO.LOW)
      time.sleep(0.05)
      GPIO.output(pin, GPIO.HIGH)

def destroy():
  for pin in pins:
    GPIO.output(pin, GPIO.HIGH)    # turn off all leds
  GPIO.cleanup()                     # Release resource


setup()


#------------------------------------------------------------------------------------------


# Multiple LED's [Refactored]
import RPi.GPIO as GPIO
import time

pins = [11, 12, 13, 15]

def setup():
  GPIO.setmode(GPIO.BOARD)      # Numbers GPIOs by physical location
  
  for pin in pins:
    GPIO.setup(pin, GPIO.OUT)   # Set all pins mode as output
    GPIO.output(pin, GPIO.HIGH) # Set all pins to high(+3.3V)

def loop():
  while True:
    for pin in pins:
      GPIO.output(pin, GPIO.LOW)  
      time.sleep(0.05)
      GPIO.output(pin, GPIO.HIGH)
    for pin in reversed(pins):
      GPIO.output(pin, GPIO.LOW)
      time.sleep(0.05)
      GPIO.output(pin, GPIO.HIGH)

def destroy():
  for pin in pins:
    GPIO.output(pin, GPIO.HIGH)    # turn off all leds
  GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
