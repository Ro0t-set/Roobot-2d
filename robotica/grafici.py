#!/usr/bin/env python
import matplotlib.pyplot as plt
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roobot.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

import math
import string
from app.models import Grafico
from django.shortcuts import get_object_or_404

x= (list(Grafico.objects.all().values_list('x', flat=True)))
print(x)

y= (list(Grafico.objects.all().values_list('y', flat=True)))
print(y)

plt.plot(x, y, 's')
plt.axis([0, 31, 0, 31])
plt.show()
