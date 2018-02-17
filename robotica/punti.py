#!/usr/bin/env python
import os
import sys

if name == "main":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roobot.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

import math
import string
from app.models import Puntini
from django.shortcuts import get_object_or_404



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