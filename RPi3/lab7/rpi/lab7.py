import RPi.GPIO as GPIO 
from time import sleep 
import Adafruit_DHT
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
from datetime import datetime
import json

# initialize GPIO
pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)          # to use Raspberry Pi BCM pin numbers
GPIO.cleanup()

AWS_IOT_CLIENT_ID = 'humidity-temperature' 
AWS_IOT_THING_NAME = 'alexa_dht22_thing' 

# Custom Shadow callback
def customShadowCallback_Update(payload, responseStatus, token):
    if responseStatus == "timeout":
        print("Update request " + token + " time out!")
    if responseStatus == "accepted":
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("Update request with token: " + token + " accepted!")
        print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    if responseStatus == "rejected":
        print("Update request " + token + " rejected!")



# This should be set to your accounts endpoint
AWS_IOT_ENDPOINT = ''
AWS_IOT_ROOT_CA = '/home/pi/workspace/alexa_temp_hdt/VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem'
AWS_IOT_PRIVATE_KEY = '/home/pi/workspace/alexa_temp_hdt/0c01d13c42-private.pem.key'
AWS_IOT_CERTIFICATE = '/home/pi/workspace/alexa_temp_hdt/0c01d13c42-certificate.pem.crt'


# AWS IoT certificate based connection
myMQTTClient = AWSIoTMQTTShadowClient(AWS_IOT_CLIENT_ID)
myMQTTClient.configureEndpoint(AWS_IOT_ENDPOINT, 8883)
myMQTTClient.configureCredentials(AWS_IOT_ROOT_CA, AWS_IOT_PRIVATE_KEY, AWS_IOT_CERTIFICATE)
myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
 
#connect
myMQTTClient.connect()

# Create a deviceShadow with persistent subscription
deviceShadowHandler = myMQTTClient.createShadowHandlerWithName(AWS_IOT_THING_NAME, True)

 
def getSensorData(): 
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin) 
    return (str(round(RH, 2)), str(round(T, 2)))

def main(): 
    print ('gathering sensor data\n')
   
    while True: 
        try: 
            RH, T = getSensorData() 
            print ("Temp = " + str(T) + " Humidity = " + str(RH) + "\n") 
            now = datetime.now()
            time_date = now.strftime('%H:%M:%S %m-%d-%Y') #e.g. 00:54:42 03-19-2018
            Payload =     {
                            "state": {
                              "reported": {
                                "timestamp": time_date,
                                "temperature": str(T),
                                "humidity": str(RH)
                              }
                            }
                          }
            JSONPayload = json.dumps(Payload, indent=4)              
            deviceShadowHandler.shadowUpdate(JSONPayload, customShadowCallback_Update, 5)
            print ("payload", JSONPayload)
            print ("\n\n")
            sleep(60)     #uploads DHT22 sensor values every 1 minute
        except: 
            print ('exiting')
            break 

# call main 
if __name__ == '__main__': 
   main()