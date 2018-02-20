#!/usr/bin/env python
import os
import sys
import math

import string
from app.models import Puntini
from django.shortcuts import get_object_or_404

if name == "main":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roobot.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

Puntini.objects.create(nord=nord, sud=sud, est=est, overt=overt)

# While (cas(x,y) = 0):
#  cas(x,y) = 1
#
#  while angolo < 360:
#    attiva sensore
#    se c'è un ostacolo:
#      calcola coordinate ostacolo

#      approssimale a interi ottenendo x1 e y1
#      cas(x1,y1) = 2
#    angolo = angolo+15
#  angolo=0
#
#  While (cas(x,y)) = 1):
#    While (una delle caselle in un certo rettangolo davanti è nello stato 2):
#
#      girati a destra o sinistra casualmente
#    se destra:
#      se nord -> est
#      se est -> sud
#      se sud -> ovest
#      se ovest -> nord
#    se sinistra:
#      se nord -> ovest
#      se ovest -> sud
#      se sud -> est
#      se est -> nord
#
#    Vai avanti di 3m
#      se nord: y=y+3
#      se sud: y=y-3
#      se est: x=x+3
#      se ovest: x=x-3

#1 = no obstacles
#2 = obstacles
#3 = robot

def getXCorFromDistance(distance, angle):
    x = Int(cos(angle)*distance)
    return x
def getYCorFromDistance(distance, angle):
    y = Int(sin(angle)*distance)
    return y

def initCorSystemFromDistances(distances):
    plot = dict() #init with no obstacles
    for x in range(-20, 20):
        newRow = dict()
        for y in range(-20, 20):
            if x == 0 & y == 0:
                newRow[y] = 3
            else:
                newRow[y] = 1
        plot[x] = newRow
    angle = 0.0
    count = 0
    pi = math.pi
    while angle < (2.0*pi):
        angle = (angle+(2.0*pi)/float(distances.count))
        x = getXCorFromDistance(distances[count], angle)
        y = getYCorFromDistance(distances[count], angle)
        plot[x][y] = 2
        count = count+1
    return plot

class Tile():
    column = Int()
    row = Int()
    tileType = Int() #enum if possible
