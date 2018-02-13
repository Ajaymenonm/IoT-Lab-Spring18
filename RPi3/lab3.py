#park sensor without buzzer

import RPi.GPIO as GPIO                     
import time                                 

trigger_pin = 23                                 
echo_pin = 24                                   
red_pin = 22
yellow_pin = 27
green_pin = 17

def setup():                              #method to setup pins and make led's low initially
  GPIO.setmode(GPIO.BCM)                     
  GPIO.setup(echo_pin, GPIO.IN)                   
  GPIO.setup(trigger_pin, GPIO.OUT)                  
  GPIO.setup(red_pin, GPIO.OUT)                  
  GPIO.setup(yellow_pin, GPIO.OUT)                  
  GPIO.setup(green_pin, GPIO.OUT)                  
  GPIO.output(green_pin, GPIO.LOW)
  GPIO.output(yellow_pin, GPIO.LOW)
  GPIO.output(red_pin, GPIO.LOW)
  

def red():
  GPIO.output(red_pin, GPIO.HIGH)
  GPIO.output(green_pin, GPIO.LOW)
  GPIO.output(yellow_pin, GPIO.LOW)

def yellow():
  GPIO.output(yellow_pin, GPIO.HIGH)
  GPIO.output(red_pin, GPIO.LOW)
  GPIO.output(green_pin, GPIO.LOW)

def green():
  GPIO.output(green_pin, GPIO.HIGH)
  GPIO.output(yellow_pin, GPIO.LOW)
  GPIO.output(red_pin, GPIO.LOW)

def calculate_distance():
  while True:

    GPIO.output(trigger_pin, False)                   #set trigger_pin as LOW
    print ("Giving delay between distance measuring cycle")
    time.sleep(0.5)                          

    GPIO.output(trigger_pin, True)                  #set trigger_pin as HIGH
    time.sleep(0.00001)                      
    GPIO.output(trigger_pin, False)                 

    while GPIO.input(echo_pin)==0:               #check if echo_pin is LOW
      pulse_start = time.time()                  #saves the last known time of LOW pulse

    while GPIO.input(echo_pin)==1:               #Check if echo_pin is HIGH
      pulse_end = time.time()                    #saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start    #get pulse duration to a variable
    distance = pulse_duration * 17150           #multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)               #round to two decimal points

    print ("Distance:",distance - 0.5,"cm")     #print distance with 0.5 cm calibration
    
    if distance <= 5:                          #call red method if distance is less than or equal to 5cm
      red()

    elif 6 <= distance < 20:                   #call yellow method if distance is greater than 6cm and less than 20cm
      yellow()

    elif 21 <= distance < 150:                 #call green method if distance is greater than 21cm and less than 150cm
      green()

    else:
      print("Out of Range")

if __name__ == '__main__':                      # Program starts from here
  
  print('Press Ctrl+C to end the program...')
  setup()
  
  try:
    print('calling loop')
    calculate_distance()
  except KeyboardInterrupt:
    print('cleaningup gpio pins')
    GPIO.cleanup()

#=============================================================================================================================

#park sensor with buzzer

import RPi.GPIO as GPIO                     
import time                                 

trigger_pin = 23                                 
echo_pin = 24                                   
red_pin = 22
yellow_pin = 27
green_pin = 17
buzzer_pin = 25

def setup():                                        #method to setup pins and make led's low initially
  GPIO.setmode(GPIO.BCM)                     
  GPIO.setup(echo_pin, GPIO.IN)                   
  GPIO.setup(trigger_pin, GPIO.OUT)                  
  GPIO.setup(red_pin, GPIO.OUT)                  
  GPIO.setup(yellow_pin, GPIO.OUT)                  
  GPIO.setup(green_pin, GPIO.OUT)                  
  GPIO.setup(buzzer_pin, GPIO.OUT)
  GPIO.output(green_pin, GPIO.LOW)
  GPIO.output(yellow_pin, GPIO.LOW)
  GPIO.output(red_pin, GPIO.LOW)
  

def red():
  GPIO.output(red_pin, GPIO.HIGH)
  GPIO.output(green_pin, GPIO.LOW)
  GPIO.output(yellow_pin, GPIO.LOW)
  GPIO.output(buzzer_pin, GPIO.LOW)
  time.sleep(0.1)
  GPIO.output(buzzer_pin, GPIO.HIGH)
  time.sleep(0.1)

def yellow():
  GPIO.output(yellow_pin, GPIO.HIGH)
  GPIO.output(red_pin, GPIO.LOW)
  GPIO.output(green_pin, GPIO.LOW)
  GPIO.output(buzzer_pin, GPIO.LOW)
  time.sleep(0.5)
  GPIO.output(buzzer_pin, GPIO.HIGH)
  time.sleep(0.5)

def green():
  GPIO.output(green_pin, GPIO.HIGH)
  GPIO.output(yellow_pin, GPIO.LOW)
  GPIO.output(red_pin, GPIO.LOW)
  GPIO.output(buzzer_pin, GPIO.LOW)

def calculate_distance():
  while True:

    GPIO.output(trigger_pin, False)                 #set trigger_pin as LOW
    print ("Giving delay between distance measuring cycle")
    time.sleep(0.5)                          

    GPIO.output(trigger_pin, True)                  #set trigger_pin as HIGH
    time.sleep(0.00001)                      
    GPIO.output(trigger_pin, False)                 

    while GPIO.input(echo_pin)==0:                  #check if echo_pin is LOW
      pulse_start = time.time()                     #saves the last known time of LOW pulse

    while GPIO.input(echo_pin)==1:                  #Check if echo_pin is HIGH
      pulse_end = time.time()                       #saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start        #get pulse duration to a variable
    distance = pulse_duration * 17150               #multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)                   #round to two decimal points

    print ("Distance:",distance - 0.5,"cm")         #print distance with 0.5 cm calibration

    GPIO.output(buzzer_pin, GPIO.LOW)
    
    if distance <= 5:                               #call red method if distance is less than or equal to 5cm
      red()

    elif 6 <= distance < 20:                        #call yellow method if distance is greater than 6cm and less than 20cm
      yellow()

    elif 21 <= distance < 150:                      #call green method if distance is greater than 21cm and less than 150cm
      green()

    else:
      print("Out of Range")

if __name__ == '__main__':                          # Program starts from here
  
  print('Press Ctrl+C to end the program...')
  setup()
  
  try:
    print('calling loop')
    calculate_distance()
  except KeyboardInterrupt:
    print('cleaningup gpio pins')
    GPIO.cleanup()