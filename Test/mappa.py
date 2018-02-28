import Serial
import math 
import os


def distance():
	a=0
	while a<36:
		a=str(a)
		distance="read"+a
		distance="Serial."+distance
		distance=eval(distance)
		a=int(a)
		angle=10*a
		a=a+1

		

def getXCorFromDistance(distance):
	x = Int(cos(distance.angle)*distance.distance)
	print (x)

# def getYCorFromDistance(distance):
#     y = Int(sin(12)*distance)
#     return y

getXCorFromDistance()
