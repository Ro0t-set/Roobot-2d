from django import forms

from .models import Punti
from .models import Mappa
from .models import Grafico

class MappaForm(forms.ModelForm):
    class Meta:
        model = Mappa
        fields = ('nome_mappa',)
        widgets = {
                'nome_mappa': forms.TextInput(attrs={'class': 'form-control'}),
            }


class AmpiezzaForm(forms.Form):
    ampiezza = forms.IntegerField()
    widgets = {
            'ampiezza': forms.TextInput(attrs={'class': 'form-control col-form-label'}),
        }
