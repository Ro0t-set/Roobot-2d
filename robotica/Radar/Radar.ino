#include <NewPing.h>
#include <Servo.h>

#define TRIGGER_PIN0  5
#define ECHO_PIN0  7
#define TRIGGER_PIN1  6
#define ECHO_PIN1  8
#define MAX_DISTANCE  400

int Mseconds0 = 0;
int Mseconds1 = 0;
int Distance0 = 0;
int Distance1 = 0; 
int angolo;


NewPing sonar0(TRIGGER_PIN0, ECHO_PIN0, MAX_DISTANCE); //Oggetto sonar 1
NewPing sonar1(TRIGGER_PIN1, ECHO_PIN1, MAX_DISTANCE); //Oggetto sonar 2

Servo servomotore;

void setup(){
Serial.begin (115200); //Comunicazione seriale 115200 bit
servomotore.attach(3);
pinMode(2,OUTPUT);
pinMode(12,OUTPUT);
digitalWrite(2,HIGH);
digitalWrite(12,HIGH);
servomotore.write(180);
}
/*Il loop comprende due funzioni; sensori e Mappa, attivate ogni 15 gradi di movimento del servomotore, 
sensori rileva le distanze, Mappa invia i valori al seriale, ogni ciclo del radar produce 24 valori in centimetri*/
void loop() {
  
angolo = 0;
while(angolo<180)
{
   angolo = angolo+5;
   servomotore.write(angolo);
   sensori();
   Mappa();
   delay(1000);

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
}
