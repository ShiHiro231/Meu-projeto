from django import forms

class UserForm(forms.Form):
    usuario = forms.CharField(label='Digite seu nome', max_length=100)
    # IntegerField não aceita traços e parênteses, então é melhor usar CharField para o telefone
    telefone = forms.CharField(label='Digite seu Telefone', max_length=15) 