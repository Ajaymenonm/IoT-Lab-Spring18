#Data logger stored on RPi

import RPi.GPIO as GPIO
import time
import datetime

ldr_pin = 7
log_interval = 1                                          #in seconds
  
file_name = "data_logger.txt"
open(file_name, 'w').close()

GPIO.setmode(GPIO.BOARD)


def loop():
    while True:
        for x in range (1, 6):
          if x == 5:
            ldr = recharge_time(ldr_pin)                                        #call recharge time method
            print(ldr)
            
            data_to_write = (str(datetime.datetime.now()) + " , " + str(ldr))   #format data to write
            write_to_file(data_to_write, file_name)                             #call write to file method
        
        time.sleep(log_interval)


def recharge_time(ldr_pin):
    count = 0                                             #initialize counter to zero
  
    GPIO.setup(ldr_pin, GPIO.OUT)                         #initially set it to Output
    GPIO.output(ldr_pin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(ldr_pin, GPIO.IN)                          #change the pin back to input 
    
    while (GPIO.input(ldr_pin) == GPIO.LOW):              #count until the pin goes high
        count += 1

    return count


def write_to_file(text, file): 
    f = open(file,'a')                                    #open file with append option
    f.write(text+'\n')
    f.close()


if __name__ == '__main__':
    try:
      loop()
    except KeyboardInterrupt:
      GPIO.cleanup()


#===================================================================================================================

#Data logger stored on ThingSpeak

import RPi.GPIO as GPIO
import time
import datetime
import requests

ldr_pin = 7
log_interval = 1                                                  

GPIO.setmode(GPIO.BOARD)


def loop():
    while True:
      for x in range (1, 6):
        if x == 5:
          ldr = recharge_time(ldr_pin)                               
          print(ldr)
          
          r = requests.get("https://api.thingspeak.com/update?api_key=YKSU7xxxxxxxxxxxld1=" + str(ldr))  #send data to endpoint
      
      time.sleep(log_interval)


def recharge_time (pin_ldr):
    count = 0
  
    GPIO.setup(pin_ldr, GPIO.OUT)
    GPIO.output(pin_ldr, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(pin_ldr, GPIO.IN)
  
    while (GPIO.input(pin_ldr) == GPIO.LOW):
        count += 1

    return count


if __name__ == '__main__':

    try:
      loop()
    except KeyboardInterrupt:
      GPIO.cleanup()
