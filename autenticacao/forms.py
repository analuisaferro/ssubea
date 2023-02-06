from django import forms
from django.forms import ModelForm
from .models import *
from .functions import validate_cpf

class Form_Tutor(ModelForm):
    class Meta:
        model = Tutor
        widgets = {
            'dt_nascimento':forms.TextInput(attrs={'type':'date'}),
            'cpf':forms.TextInput(attrs={'onkeydown':'mascara(this, icpf)'}),
            'telefone':forms.TextInput(attrs={'onkeydown':'mascara(this, itel)'})


        }
        exclude = ['dt_inclusao', 'user']

    def clean_cpf(self):
        cpf = validate_cpf(self.cleaned_data["cpf"])
        return cpf

    def clean_telefone(self):
        telefone = self.cleaned_data["telefone"]
        telefone = telefone.replace('(', '')
        telefone = telefone.replace(' ', '')
        telefone = telefone.replace(')', '')
        telefone = telefone.replace('-', '')
        return telefone


