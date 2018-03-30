#include <ESP8266WiFi.h>
#include <AmazonIOTClient.h>
#include <ESP8266AWSImplementations.h>

Esp8266HttpClient httpClient;
Esp8266DateTimeProvider dateTimeProvider;

AmazonIOTClient iotClient;
ActionError actionError;

const char* ssid = "";
const char* password = "";

/*===============Ultrasonic======================*/
int echoPin = D0; // Echo Pin
int trigPin = D1; // Trigger Pin
long duration;
long distance; // Duration used to calculate distance
/*=============================================*/


void initWLAN()
{
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
  }
}

void initAWS()
{
  iotClient.setAWSRegion("us-east-1");
  iotClient.setAWSEndpoint("amazonaws.com");
  iotClient.setAWSDomain("");
  iotClient.setAWSPath("/things/IoTDevice/shadow");
  iotClient.setAWSKeyID("");
  iotClient.setAWSSecretKey("P");
  iotClient.setHttpClient(&httpClient);
  iotClient.setDateTimeProvider(&dateTimeProvider);
}

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.println("begin");
  initWLAN();
  Serial.println("wlan initialized");
  initAWS();
  Serial.println("iot initialized");
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop()
{
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);   
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);  
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);  
  //Calculate the distance (in cm) based on the speed of sound.
  distance = duration/58.2;
  delay (50);
  Serial.println(distance);  
  //strcpy(shadow, "{\"state\":{\"reported\":{\"Tank_Level\": 911}}}");
   String test1 = String ("{\"state\":{\"reported\":{\"Tank_Level\":");
  String test2 = String("}}}");
  String dis = String(distance);
  test1 += dis;
  test1 += test2;
  char shadow[100];
  test1.toCharArray(shadow, 100);

 // sprintf(shadow, "%d", distance);
  Serial.println("Trying to send data");
  Serial.print(shadow);
  
  char* result = iotClient.update_shadow(shadow, actionError);
  Serial.print(result);
  
  delay(30000);
}