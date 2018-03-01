#!/usr/bin/env python
import TestSerial
import math
import os
import sys
import django

from django.shortcuts import get_object_or_404

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roobot.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

from app.models import Mappa
nome_mappa =input(str("nome mappa:"))
def distance():
	a=0
	angle = 0.0
	while a<36:
		a=str(a)
		distance="read"+a
		distance="TestSerial."+distance
		distance=eval(distance)
		a=int(a)
		angle += (math.pi*2)/ 36.0
		x = int(math.cos(angle)*distance)
		y = int(math.sin(angle)*distance)
		print (x)
		print (y)
		a= a+1
		try:
			quadrato=Mappa.objects.get(x=x, y=y, nome_mappa=nome_mappa)
			quadrato.aggettivo=2
			quadrato.save()


			print(quadrato)
		except:
			pass


grafo=Mappa.objects.filter(nome_mappa=nome_mappa, aggettivo=2)
print(grafo)
distance()

# def getYCorFromDistance(distance):
#     y = Int(sin(12)*distance)
#     return y
