import matplotlib.pyplot as plt
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roobot.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

import math
import string
from app.models import Mappa
from django.shortcuts import get_object_or_404
nome_mappa=3

x= (list(Mappa.objects.filter(nome_mappa=nome_mappa, aggettivo=11).values_list('x', flat=True)))
print(x)

y= (list(Mappa.objects.filter(nome_mappa=nome_mappa, aggettivo=11).values_list('y', flat=True)))
print(y)

plt.plot(x, y, 's')
plt.axis([-20, 20, 20, -20])
plt.show()