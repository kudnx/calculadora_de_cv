from django import forms

class CalculadoraForm(forms.Form):
    dano_critico = forms.FloatField(label='Dano Critico')
    taxa_critica = forms.FloatField(label='Taxa Critica')
