from django.contrib import admin
from .models import Punti, Mappa, Nome, Grafico

# Register your models here.

admin.site.register(Punti)
admin.site.register(Mappa)
admin.site.register(Grafico)
admin.site.register(Nome)
