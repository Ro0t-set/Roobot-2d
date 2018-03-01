from django import forms

from .models import Punti, Mappa, Grafico, Nome


class MappaForm(forms.ModelForm):
    class Meta:
        model = Mappa
        fields = ()

class NomeForm(forms.ModelForm):
    class Meta:
        model = Nome
        fields = ('nome_mappa',)

class AmpiezzaForm(forms.Form):
    ampiezza = forms.IntegerField()
    widgets = {
            'ampiezza': forms.TextInput(attrs={'class': 'form-control'}),
        }
