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
        if name:
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
        
class Form_Errante(ModelForm):
    class Meta:
        model = Errante

        exclude = ['dt_inclusao', 'especie']
        widgets = {
            'tipo':forms.RadioSelect(),
        }

class Form_Info_Extras(ModelForm):
    class Meta:
        model = Info_Extras
        fields = ['alimentacao_tipo', 'alimentacao_periodo', 'condicoes', 'dt_vacinacao', 'dt_vermifugacao', 'complemento', 'dt_registro']
        widgets = {
            'alimentacao_periodo':forms.RadioSelect(),
        }