from django import forms
from django.forms import ModelForm
from .models import *


class Form_Tutor(ModelForm):
    class Meta:
        model = Tutor
        widgets = {
            'dt_nascimento':forms.TextInput(attrs={'type':'date'})
        }
        exclude = ['dt_inclusao', 'user']
    # def clean_cpf(self):
    #     cpf = validate_CPF(self.cleaned_data["cpf"])
    #     cpf = cpf.replace('.', '')
    #     cpf = cpf.replace('-', '')
    #     return cpf