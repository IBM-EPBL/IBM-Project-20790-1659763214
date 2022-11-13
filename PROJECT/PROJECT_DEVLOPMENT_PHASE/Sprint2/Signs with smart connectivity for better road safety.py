import time
import sys
import ibmiotf.application
import ibmiotf.device

#provide your ibm watson Device credentials  
organization = "vd4xhx"
devicetype="mathaniza1234"
deviceid="christian"
authmethod="token"
authtoken="JLJdQ8p?5Rizji2Xa"

#Initialize GPIO

def myCommandCallBack(cmd):
    print("Command received: %s"% cmd.data('command')
    print(cmd)


         
/*
   PIR sensor tester
*/

(9600);
}

void loop() {int ledPin = 13;                // choose the pin for the LED
int inputPin = 2;               // choose the input pin (for PIR sensor)
int pirState = LOW;             // we start, assuming no motion detected
int val = 0;                    // variable for reading the pin status

void setup() {
  pinMode(ledPin, OUTPUT);      // declare LED as output
  pinMode(inputPin, INPUT);     // declare sensor as input

  Serial.begin
  val = digitalRead(inputPin);  // read input value
  if (val == HIGH) {            // check if the input is HIGH
    digitalWrite(ledPin, HIGH);  // turn LED ON
    if (pirState == LOW) {
      // we have just turned on
      Serial.println("Motion detected!");
      // We only want to print on the output change, not state
      pirState = HIGH;
    }
  } else {
    digitalWrite(ledPin, LOW); // turn LED OFF
    if (pirState == HIGH) {
      // we have just turned of
      Serial.println("Motion ended!");
      // We only want to print on the output change, not state
      pirState = LOW;
    }
  }
}

             
import json
#replace the url and it should be in""
a="https://api.openweathermap.org/data/2.5/weather?q=chennai,%20IN&appid=bc453a0b339cb9ee1ad10d2dd64d0bc0"
r=requests.get(url=a)
print(r)
data =r.json ()
tem=data ('main')('h')                
print(tem)

/*
  HC-SR04 Ultrasonic Sensor Example.

  Turn the LED on when an object is within 100cm range.

  Copyright (C) 2021, Uri Shaked
*/

#define ECHO_PIN 2
#define TRIG_PIN 3

void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

float readDistanceCM() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  int duration = pulseIn(ECHO_PIN, HIGH);
  return duration * 0.034 / 2;
}

void loop() {
  float distance = readDistanceCM();

  bool isNearby = distance < 100;
  digitalWrite(LED_BUILTIN, isNearby);

  Serial.print("Measured distance: ");
  Serial.println(readDistanceCM());

  delay(100);
}


DEMO using the server test.mosquitto.org

You can use any MQTT client with the following settings
Server : test.mosquitto.org
no login / no password
port: 1883 or 8081 for websocket
Topic: /AnnexTest
Subscribe: /AnnexTx
 
Or you can use the free MQTT online client

https://www.cicciocb.com/MQTT/

this is already configured so just
- click on Connect
- write your message in "Publish Message"
- Press "Publish" to send your message that will be shown in the scrolling display
- Click on Subscribe to receive the temperature sensor data


# Disconnect the device and the application from the cloud
devicecli.disconnect()             

