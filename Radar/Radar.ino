#include <NewPing.h>
#include <Servo.h>

#define TRIGGER_PIN0  5
#define ECHO_PIN0  7
#define TRIGGER_PIN1  6
#define ECHO_PIN1  8
#define MAX_DISTANCE  100


int laser = 10;
int Mseconds0 = 0;
int Mseconds1 = 0;
int Distance0 = 0;
int Distance1 = 0; 
int angolo;




NewPing sonar0(TRIGGER_PIN0, ECHO_PIN0, MAX_DISTANCE); //Oggetto sonar 1
NewPing sonar1(TRIGGER_PIN1, ECHO_PIN1, MAX_DISTANCE); //Oggetto sonar 2

Servo servomotore;

void setup(){
Serial.begin (115200); 
servomotore.attach(3);
pinMode(2,OUTPUT);
pinMode(12,OUTPUT);
pinMode(laser,OUTPUT);
digitalWrite(2,HIGH);
digitalWrite(12,HIGH);
servomotore.write(0);
Serial.println("Ready");
}
/*Il loop comprende due funzioni; sensori e Mappa, attivate ogni 5 gradi di movimento del servomotore, 
sensori rileva le distanze, Mappa invia i valori al seriale, ogni ciclo del radar produce 24 valori in centimetri*/
void loop() {
  Blink();
 
if (Serial.available() > 0){


angolo=0;
 
while(angolo<180)
{  
   digitalWrite(laser,HIGH);
   angolo = angolo+5;
   servomotore.write(angolo);
   sensori();
   Mappa();
   delay(500);
  
}
Serial.end();
servomotore.write(0);

}
}
 

void Mappa(){
  Serial.println(Distance0);
  Serial.println(Distance1);
  }  
void sensori(){
   Mseconds0 = sonar0.ping_median(5);
   Mseconds1 = sonar1.ping_median(5);
   Distance0 = sonar0.convert_cm(Mseconds0);
   Distance1 = sonar1.convert_cm(Mseconds1);
    while (Distance0 == 0)
 {
   Distance0 = 101;
  }
  while (Distance1 == 0)
 {
   Distance1 = 101;
  }
}
void Blink(){
  digitalWrite(laser, HIGH);
  delay(500);
  digitalWrite(laser, LOW);
  delay(500);
  
  }
