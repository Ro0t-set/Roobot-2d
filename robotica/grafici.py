#!/usr/bin/env python
import matplotlib.pyplot as plt
import os
import sys
import matplotlib.pyplot as plt

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roobot.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


x= (list(x.values_list('x', flat=True)))
print(x)

y= (list(y.values_list('y', flat=True)))
print(y)

plt.plot(x, y, 's')
plt.axis([0, 300, 0, 300])
plt.show()
