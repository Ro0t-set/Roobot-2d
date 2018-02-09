#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roobot.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

import math
import string
from app.models import Puntini
from django.shortcuts import get_object_or_404



Puntini.objects.create(nord=nord, sud=sud, est=est, overt=overt)







