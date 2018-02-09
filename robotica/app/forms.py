from django import forms

from .models import Punti
from .models import Mappa
from .models import Grafico

class MappaForm(forms.ModelForm):
    class Meta:
        model = Mappa
        fields = ('nome_mappa',)


class AmpiezzaForm(forms.Form):
    ampiezza = forms.IntegerField()
