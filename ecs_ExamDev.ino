#include<Servo.h>
Servo myservo;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
myservo.attach(9);
pinMode(8, OUTPUT);
digitalWrite(8,HIGH);
myservo.write(0);
}

void loop()
{
  if(Serial.read()=='a')
  {
    moveRoller();
    //delay(500);
    
  }
}

void moveRoller() {
    digitalWrite(8,LOW);
    delay(1000);
    moveServo();
    digitalWrite(8,HIGH);
}

void moveServo()
{
  int pos=0;
  for (pos = 0; pos <= 360; pos += 1) 
  {
    myservo.write(pos);       
    delay(10);                 
  }
  for (pos = 360; pos >= 0; pos -= 1) 
  {
    myservo.write(pos);              
    delay(1);                       
  }
}
