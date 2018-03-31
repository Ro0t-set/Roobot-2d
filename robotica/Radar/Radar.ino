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

char buffer[80] = { 0 };
void setup(){
Serial.begin (115200); //Comunicazione seriale 115200 bit
servomotore.attach(3);
pinMode(2,OUTPUT);
pinMode(12,OUTPUT);
pinMode(13,OUTPUT);
digitalWrite(2,HIGH);
digitalWrite(12,HIGH);
servomotore.write(180);
Serial.println("test");
}
/*Il loop comprende due funzioni; sensori e Mappa, attivate ogni 15 gradi di movimento del servomotore, 
sensori rileva le distanze, Mappa invia i valori al seriale, ogni ciclo del radar produce 24 valori in centimetri*/
void loop() {

if (Serial.available() > 0) {
  
  
  Serial.readBytesUntil('\n', buffer, sizeof(buffer));
  Serial.println(buffer);
  int incremento = atoi(buffer);
  memset(buffer, 0, sizeof(buffer));
 // Serial.print("valore inserito = ");
 // Serial.println(incremento);
angolo = 0;
while(angolo<180)
{
   angolo = angolo+incremento;
   digitalWrite(13,HIGH);
   servomotore.write(angolo);
   sensori();
   Mappa();
   delay(700);
   digitalWrite(13,LOW);
}
}
}
void Mappa(){
  Serial.println(Distance0);
  Serial.println(Distance1);
  Serial.print("angolo = ");//commenta questa riga dopo aver eseguito il test
  Serial.println(angolo);//commenta questa riga dopo aver eseguito il test
}  
void sensori(){
   Mseconds0 = sonar0.ping_median(5);
   Mseconds1 = sonar1.ping_median(5);
   Distance0 = sonar0.convert_cm(Mseconds0);
   Distance1 = sonar1.convert_cm(Mseconds1);
}
