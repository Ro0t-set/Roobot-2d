import TestSeril
import math
import os


def distance():
	a=0
	angle = 0.0
	while a<36:
		a=str(a)
		distance="read"+a
		distance="TestSeril."+distance
		distance=eval(distance)
		a=int(a)
		x = int(math.cos(angle)*distance)
		print (x)
		angle += (math.pi*2)/ 36.0
		a= a+1
		

distance()

# def getYCorFromDistance(distance):
#     y = Int(sin(12)*distance)
#     return y
