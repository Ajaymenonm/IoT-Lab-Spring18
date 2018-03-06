from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import RPi.GPIO as GPIO
import time

pin = 11
GPIO.setmode(GPIO.BOARD)        # to use Raspberry Pi board pin numbers
GPIO.setup(pin, GPIO.OUT)
GPIO.setwarnings(False)

AWS_IOT_SUBSCRIBE_TOPIC = 'alexa-rpi'
AWS_IOT_CLIENT_ID = 'alexa-led'


# Custom MQTT message callback
def custom_callback(client, userdata, message):

    print("--------------")
    print("Received a new message: ", message.payload)
    print("from topic: ", message.topic)
    print("--------------\n\n")

    if message.payload == 'On':
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)


# This should be set to your accounts endpoint
AWS_IOT_ENDPOINT = 'xxx'
AWS_IOT_ROOT_CA = 'xxx'
AWS_IOT_PRIVATE_KEY = 'xxx'
AWS_IOT_CERTIFICATE = 'xxx'

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = AWSIoTMQTTClient(AWS_IOT_CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(AWS_IOT_ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(AWS_IOT_ROOT_CA, AWS_IOT_PRIVATE_KEY, AWS_IOT_CERTIFICATE)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe(AWS_IOT_SUBSCRIBE_TOPIC, 1, custom_callback)


if __name__ == '__main__':
  try:
      while True:    
        time.sleep(1)
  except KeyboardInterrupt:
      GPIO.cleanup()
