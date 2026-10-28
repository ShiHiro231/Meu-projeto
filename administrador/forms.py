from django import forms

class UserForm(forms.Form):
    usuario = forms.CharField(label= 'Digite seu nome',max_length=100)
    telefone = forms.IntegerField(label='Digite seu Telefone', max_value=14)