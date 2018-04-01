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
        widgets = {
                'nome_mappa': forms.TextInput(attrs={'class': 'text'}),
                }



class AmpiezzaForm(forms.Form):
    ampiezza = forms.IntegerField()
    fields = ('ampiezza')
    widgets = {
            'ampiezza': forms.NumberInput(attrs={'class': 'form-control text'}),
        }

class DensitàForm(forms.Form):
    densità = forms.IntegerField( min_value=5, max_value=20, initial=5)
    fields = ('densità')
