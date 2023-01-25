import unicodedata
from django import forms
from django.forms import ModelForm
from .models import *


class Form_Tipo(ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome']


class Form_Especie(ModelForm):
    class Meta:
        model = Especie
        fields = ['nome_especie']
        
    def clean_nome_especie(self):
        name = self.cleaned_data.get('nome_especie')
        name = name.lower()
        name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode()
        return name


class Form_Animal(ModelForm):    

    class Meta:
        model = Animal
        
        exclude = ['dt_inclusao', 'especie']
        widgets = {
                'tutor': forms.HiddenInput(), 
                'tipo': forms.RadioSelect()}