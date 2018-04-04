#!/usr/bin/env python
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
y=0
while y<1001:
	y=y+1
	x=0
	while x<1001:
		x=x+1
		Mappa.objects.create(x=x, y=y)







