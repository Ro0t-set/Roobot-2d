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
