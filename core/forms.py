from django import forms
from django.forms import ModelForm
from .models import *

class Form_Local(ModelForm):
    class Meta:
        model = Local
        fields = '__all__'

class Form_Tipo(ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome']

class Form_Animal(ModelForm):    
    class Meta:
        model = Animal
        exclude = ['dt_inclusao']

class Form_Ave(ModelForm):
    class Meta:
        model = Ave
        exclude = []

class Form_Tutor(ModelForm):
    class Meta:
        model = Tutor
        widgets = {
            'dt_nascimento':forms.TextInput(attrs={'type':'date'})
        }
        exclude = ['dt_inclusao']
