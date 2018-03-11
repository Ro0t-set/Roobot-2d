#!/usr/bin/python
# -*- coding: UTF8 -*-

# se si vuole usare quasto codice in test sensa i sensori sostituire tutti i "Serial" con "TestSerial"
import serial
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
nome_mappa =input(str("nome mappa:"))#selezionare l'id della mappa su cui si creerà il grafico
def distance():
	#loop di lettura dei dati distanze dal seriale
	Rad180=((math.pi)*180)/180
	a=0
	angle = 0
	while a<24:
		a=str(a)
		distance="read"+a
		distance="Serial."+distance
		distance=eval(distance)#lettura distanza
		distance=int(distance)
		a=int(a)
		angleRad= angle*(math.pi)/180#calcolo angoli motore in radianti
		if a%2 == 0:
			x = int((math.cos(angleRad)*distance)/5)#creazione x e y per mezzo di seno e coseno, da lettura a cerchio a piano cartesiano
			y = int((math.sin(angleRad)*distance)/5)
		else:
			angle=angle+15
			x = int((math.cos(angleRad+Rad180)*distance)/5)#creazione x e y per mezzo di seno e coseno, da lettura a cerchio a piano cartesiano
			y = int((math.sin(angleRad+Rad180)*distance)/5)

		print (x)
		print (y)
		a= a+1
		try:
			quadrato=Mappa.objects.get(x=x, y=y, nome_mappa=nome_mappa)#filtraggio dei dati per x, y e id mappa
			quadrato.aggettivo=26#attribuzione di un aggettivo
			quadrato.save()#salvataggio dati in Mappa


			print(quadrato)
		except:
			pass


grafo=Mappa.objects.filter(nome_mappa=nome_mappa, aggettivo=26)#filtraggio dati per aggettivo(comodo per lo sviluppo)
print(grafo)
distance()

# def getYCorFromDistance(distance):
#     y = Int(sin(12)*distance)
#     return y
