import RPi.GPIO as GPIO
import time


#sulle viwes:  import movimento,   movimento.avanti(distanzaTemporale)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT) #pin1 motore1
GPIO.setup(18, GPIO.OUT) #pin2 motore1
GPIO.setup(24, GPIO.OUT) #pin1 motore2
GPIO.setup(25, GPIO.OUT) 

def avanti(distanzaTemporale):
  GPIO.output(18, GPIO.HIGH)
  GPIO.output(25, GPIO.HIGH)
  time.sleep(distanzaTemporale)
  GPIO.output(18, GPIO.LOW)
  GPIO.output(25, GPIO.LOW)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(24, GPIO.LOW)
return 0

def indietro(distanzaTemporale):
  GPIO.output(18, GPIO.LOW)
  GPIO.output(25, GPIO.LOW)
  GPIO.output(23, GPIO.HIGH)
  GPIO.output(24, GPIO.HIGH)
  time.sleep(distanzaTemporale)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(24, GPIO.LOW)
return 0

def destra(distanzaTemporale):
  GPIO.output(18, GPIO.LOW)
  GPIO.output(25, GPIO.HIGH)
  GPIO.output(23, GPIO.HIGH)
  GPIO.output(24, GPIO.LOW)
  time.sleep(distanzaTemporale)
  GPIO.output(25, GPIO.LOW)
  GPIO.output(23, GPIO.LOW)
return 0

def sinistra(distanzaTemporale):
  GPIO.output(18, GPIO.HIGH)
  GPIO.output(24, GPIO.HIGH)
  time.sleep(distanzaTemporale)
  GPIO.output(18, GPIO.LOW)
  GPIO.output(24, GPIO.LOW)  
  GPIO.output(25, GPIO.LOW)
  GPIO.output(23, GPIO.LOW) 
return 0

def stop():
  GPIO.output(18, GPIO.LOW)
  GPIO.output(25, GPIO.LOW)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(24, GPIO.LOW)
return 0
