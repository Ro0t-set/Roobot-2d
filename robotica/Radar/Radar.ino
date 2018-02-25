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

NewPing sonar0(TRIGGER_PIN0, ECHO_PIN0, MAX_DISTANCE); //Oggetto sonar 1
NewPing sonar1(TRIGGER_PIN1, ECHO_PIN1, MAX_DISTANCE); //Oggetto sonar 2

Servo servomotore;

void setup(){
Serial.begin (115200); //Comunicazione seriale 115200 bit
servomotore.attach(3);
servomotore.write(180);
}
/*Il loop comprende due funzioni; sensori e Mappa, attivate ogni 15 gradi di movimento del servomotore, 
sensori rileva le distanze, Mappa invia i valori al seriale, ogni ciclo del radar produce 24 valori in centimetri*/
void loop() {

   sensori();        
   servomotore.write(180);
   sensori();
   Mappa();
   servomotore.write(165);
   sensori();
   Mappa();
   servomotore.write(150);
   sensori();
   Mappa();
   servomotore.write(135);
   sensori();
   Mappa();
   servomotore.write(120);
   sensori();
   Mappa();
   servomotore.write(105);
   sensori();
   Mappa();
   servomotore.write(90);
   sensori();
   Mappa();
   servomotore.write(75);
   sensori();
   Mappa();
   servomotore.write(60);
   sensori();
   Mappa();
   servomotore.write(45);
   sensori();
   Mappa();
   servomotore.write(30);
   sensori();
   Mappa();
   servomotore.write(15);
   sensori();
   Mappa();
   servomotore.write(180);

}
void Mappa(){
   Serial.print("Sensore1:");
   Serial.println(Distance0);
   Serial.print("Sensore2:");
   Serial.println(Distance1);
   Serial.println("------");
   delay(700);
}  
void sensori(){
   Mseconds0 = sonar0.ping_median(5);
   Mseconds1 = sonar1.ping_median(5);
   Distance0 = sonar0.convert_cm(Mseconds0);
   Distance1 = sonar1.convert_cm(Mseconds1);
}
