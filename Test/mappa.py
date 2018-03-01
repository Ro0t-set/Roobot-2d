import TestSeril
import math
import os


def distance():
	a=0
	angle = 0.0
	while a<36:
		#a=str(a)
		#distance="read"+a
		#distance="TestSeril."+distance
		#distance=eval(distance)
		distance=eval("TestSeril.read"+str(a))
		#a=int(a)
		x = int(math.cos(angle)*distance)
		y = int(math.sin(angle)*distance)
		print (x)
		print (y)
		a+=1
		angle += (math.pi*2)/35

distance()
