# Only Button as input

from time import sleep                                        # Library will let us put in delays
import RPi.GPIO as GPIO                                       # Import the RPi Library for GPIO pin control

button1_pin=12                                                # Button 1 is connected to physical pin 12

GPIO.setmode(GPIO.BOARD)                                      # Use Physical Pin Numbering Scheme
GPIO.setup(button1_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)      # Make button1_pin an input, Activate Pull UP Resistor

while(1):                                                     # Create an infinite Loop
  input1=GPIO.input(button1_pin)

  if input1==0:                                            # Look for button 1 press
    sleep(.1)                                             # Delay
    print ('Button 1 Pressed')                            # Notify User


#===============================================================================================================================================

# One Button One LED

from time import sleep                        # Import sleep Library
import RPi.GPIO as GPIO                       # Import GPIO Library 

button1_pin=16                                # Button 1 is connected to physical pin 16
led1_pin=22                                   # LED 1 is connected to physical pin 22
button1_state=False                           # Set Flag button1_state to indicate LED is initially off

GPIO.setmode(GPIO.BOARD)                      # Use Physical Pin Numbering Scheme
GPIO.setup(button1_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button1_pin an input, Activate Pull UP Resistor
GPIO.setup(led1_pin,GPIO.OUT)                # Make LED 1 an Output


while(1):                  # Create an infinite Loop
  input1=GPIO.input(button1_pin)
  
  if input1==0:            # Look for button 1 press
    
    if button1_state==False:                # If the LED is off
      GPIO.output(led1_pin,True)            # turn it on
      print ('Button 1 ON')
      button1_state=True              # Set Flag to show led1_pin is now On 
      sleep(.5)             # Delay
    
    else:                         # If the LED is on
      GPIO.output(led1_pin,False) # Turn LED off
      print ('Button 1 OFF')
      button1_state=False               # Set Flag to show led1_pin is now Off
      sleep(.5)
        

#===============================================================================================================================================

# Two button, Two LED

from time import sleep     # Import sleep Library
import RPi.GPIO as GPIO    # Import GPIO Library 

button1_pin=16                 # Button 1 is connected to physical pin 16
button2_pin=12                 # Button 2 is connected to physical pin 12
led1_pin=22                    # LED 1 is connected to physical pin 22
led2_pin=18                    # LED 2 is connected to physical pin 18
button1_state=False                  # Set Flag button1_state to indicate LED is initially off
button2_state=False                  # Set Flag button2_state to indicate LED is initially off

GPIO.setmode(GPIO.BOARD)   # Use Physical Pin Numbering Scheme
GPIO.setup(button1_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button1_pin an input, Activate Pull UP Resistor
GPIO.setup(button2_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button2_pin an input, Activate Pull UP Resistor
GPIO.setup(led1_pin,GPIO.OUT,) # Make LED 1 an Output
GPIO.setup(led2_pin,GPIO.OUT,) # Make LED 2 an Output


while(1):                  # Create an infinite Loop
  input1=GPIO.input(button1_pin)
  input2=GPIO.input(button2_pin)

  if input1==0:            # Look for button 1 press
    
    if button1_state==False:                # If the LED is off
      GPIO.output(led1_pin,True)# turn it on
      print ('Button 1 ON')
      button1_state=True              # Set Flag to show led1_pin is now On 
      sleep(.5)             # Delay
    
    else:                         # If the LED is on
      GPIO.output(led1_pin,False) # Turn LED off
      print ('Button 1 OFF')
      button1_state=False               # Set Flag to show led1_pin is now Off
      sleep(.5)

  if input2==0:            # Look for button 1 press
    
    if button2_state==False:                # If the LED is off
      GPIO.output(led2_pin,True)# turn it on
      print ('Button 2 ON')
      button2_state=True              # Set Flag to show led1_pin is now On 
      sleep(.5)             # Delay
    
    else:                         # If the LED is on
      GPIO.output(led2_pin,False) # Turn LED off
      print ('Button 2 OFF')
      button2_state=False               # Set Flag to show led1_pin is now Off
      sleep(.5)


#===============================================================================================================================================

# dimmable led with button -PWM

from time import sleep  # Library will let us put in delays
import RPi.GPIO as GPIO # Import the RPi Library for GPIO pin control

button1_pin=16              # Give intuitive names to our pins
button2_pin=12
led1_pin=22
led2_pin=18

GPIO.setmode(GPIO.BOARD)# We want to use the physical pin number scheme
GPIO.setup(button1_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)  # Button 1 is an input, and activate pullup resisrot
GPIO.setup(button2_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)  # Button 2 is an input, and activate pullup resistor
GPIO.setup(led1_pin,GPIO.OUT) # led1_pin will be an output pin
GPIO.setup(led2_pin,GPIO.OUT) # led2_pin will be an output pin

pwm1=GPIO.PWM(led1_pin,1000)  # We need to activate PWM on led1_pin so we can dim, use 1000 Hz 
pwm2=GPIO.PWM(led2_pin,1000)  # We need to activate PWM on led2_pin so we can dim, use 1000 Hz
pwm1.start(0)              # Start PWM at 0% duty cycle (off)             
pwm2.start(0)              # Start PWM at 0% duty cycle (off)
bright=1                   # Set initial brightness to 1%

while(1):                  # Loop Forever
  if GPIO.input(button1_pin)==0:             #If left button is pressed
    print ('Button 1 was Pressed')   # Notify User
    bright=bright/2.               # Set brightness to half
    pwm1.ChangeDutyCycle(bright)   # Apply new brightness
    pwm2.ChangeDutyCycle(bright)   # Apply new brightness
    sleep(.25)                     # Briefly Pause
    print ('New Brightness is: ',bright) # Notify User of Brightness
  if GPIO.input(button2_pin)==0:             # If button 2 is pressed
    print ('Button 2 was Pressed')   # Notify User
    bright=bright*2                # Double Brightness
    if bright>100:                 # Keep Brightness at or below 100%
      bright=100
      print ('You are at Full Bright')
    pwm1.ChangeDutyCycle(bright)  # Apply new brightness
    pwm2.ChangeDutyCycle(bright)  # Apply new brightness
    sleep(.25)                    # Pause
    print ('New Brightness is: ',bright) #Notify User of Brightness

#===============================================================================================================================================

# one button, one led [Refactored 1]

from time import sleep                                  # Import sleep Library
import RPi.GPIO as GPIO                                 # Import GPIO Library 

button1_pin=12                                              # Button 1 is connected to physical pin 12
led1_pin=18                                                 # LED 1 is connected to physical pin 18
button1_state=False                                               # Set Flag button state to indicate LED is initially off

def setup():
  GPIO.setmode(GPIO.BOARD)                                # Use Physical Pin Numbering Scheme
  GPIO.setup(button1_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)    # Make button 1 an input, Activate Pull Up Resistor
  GPIO.setup(led1_pin,GPIO.OUT)                               # Make LED 1 an Output
  
  try:
    loop()
  except KeyboardInterrupt:
    GPIO.cleanup()


def loop():
  while True:                                             # Create an infinite Loop
    input1 = GPIO.input(button1_pin)

    if input1==0:                            #Check if button 1 is pressed
      global button1_state

      if button1_state==False:
              GPIO.output(led1_pin,True)
              print ('Button 1 ON')
              button1_state=True
              sleep(.5)
      else:
              GPIO.output(led1_pin,False)
              print ('Button 1 OFF')
              button1_state=False
              sleep(.5)

setup()


#===========================================================================================================================

# one button, one led [Refactored 2]

import RPi.GPIO as GPIO
import time

LedPin = 18    # pin18 --- led
BtnPin = 12    # pin12 --- button

Led_status = 1

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
  GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def swLed(ev=None):
  global Led_status
  Led_status = not Led_status
  GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
  if Led_status == 1:
    print ('led off...')
  else:
    print ('...led on')

def loop():
  GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed, bouncetime=200) # wait for falling and set bouncetime to prevent the callback function from being called multiple times when the button is pressed
  while True:
    time.sleep(1)   # Don't do anything

def destroy():
  GPIO.output(LedPin, GPIO.HIGH)     # led off
  GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    loop()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()

#=============================================================================================================================================

# Two button, Two LED [Refactored]

from time import sleep                                  # Import sleep Library
import RPi.GPIO as GPIO                                 # Import GPIO Library 

button1_pin=16                 # Button 1 is connected to physical pin 16
button2_pin=12                 # Button 2 is connected to physical pin 12
led1_pin=22                    # LED 1 is connected to physical pin 22
led2_pin=18                    # LED 2 is connected to physical pin 18
button1_state=False                  # Set Flag button1_state to indicate LED is initially off
button2_state=False                  # Set Flag button2_state to indicate LED is initially off

def setup():
  GPIO.setmode(GPIO.BOARD)   # Use Physical Pin Numbering Scheme
  GPIO.setup(button1_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button1_pin an input, Activate Pull UP Resistor
  GPIO.setup(button2_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Make button2_pin an input, Activate Pull UP Resistor
  GPIO.setup(led1_pin,GPIO.OUT,) # Make LED 1 an Output
  GPIO.setup(led2_pin,GPIO.OUT,) # Make LED 2 an Output
  
  try:
    loop()
  except KeyboardInterrupt:
    GPIO.cleanup()


def loop():
  while(1):                  # Create an infinite Loop
    input1=GPIO.input(button1_pin)
    input2=GPIO.input(button2_pin)

    if input1==0:            # Look for button 1 press
      global button1_state

      if button1_state==False:                # If the LED is off
        GPIO.output(led1_pin,True)# turn it on
        print ('Button 1 ON')
        button1_state=True              # Set Flag to show led1_pin is now On 
        sleep(.5)             # Delay
      
      else:                         # If the LED is on
        GPIO.output(led1_pin,False) # Turn LED off
        print ('Button 1 OFF')
        button1_state=False               # Set Flag to show led1_pin is now Off
        sleep(.5)

    if input2==0:            # Look for button 1 press
      global button2_state

      if button2_state==False:                # If the LED is off
        GPIO.output(led2_pin,True)# turn it on
        print ('Button 2 ON')
        button2_state=True              # Set Flag to show led1_pin is now On 
        sleep(.5)             # Delay
      
      else:                         # If the LED is on
        GPIO.output(led2_pin,False) # Turn LED off
        print ('Button 2 OFF')
        button2_state=False               # Set Flag to show led1_pin is now Off
        sleep(.5)

setup()