#!/usr/bin/env python
import Serial
import math
import os
import sys
from app.models import Grafico
from django.shortcuts import get_object_or_404

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roobot.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)



def distance():
	a=0
	angle = 0.0
	while a<36:
		a=str(a)
		distance="read"+a
		distance="Serial."+distance
		distance=eval(distance)
		a=int(a)
		x = int(math.cos(angle)*distance)
		y = int(math.sin(angle)*distance)
		print (x)
		print (y)
		Grafico.objects.create(y=y, x=x)
		a=a+1

		angle += (math.pi*2)/ 36.0
		a= a+1
		


distance()

# def getYCorFromDistance(distance):
#     y = Int(sin(12)*distance)
#     return y
