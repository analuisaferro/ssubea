from django import forms
from django.forms import ModelForm
from .models import *
from core.models import Tutor

class Form_Pessoa(ModelForm):
    class Meta:
        model = Pessoa
        widgets = {
            'dt_nascimento':forms.TextInput(attrs={'type':'date'}),
            'cpf':forms.TextInput(attrs={'onkeydown':'mascara(this, icpf)'}),
            'telefone':forms.TextInput(attrs={'onkeydown':'mascara(this, itel)'})
        }
        fields = ['nome', 'email', 'cpf', 'telefone', 'dt_nascimento', 'bairro', 'endereco', 'complemento']

