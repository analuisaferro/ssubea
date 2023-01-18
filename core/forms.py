from django import forms
from django.forms import ModelForm
from .models import *


class Form_Tipo(ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome']

class Form_Animal(ModelForm):    
    class Meta:
        model = Animal
        tipo = forms.ChoiceField(
        widget=forms.RadioSelect(),
        
    )
        exclude = ['dt_inclusao', 'tutor']

class Form_Ave(ModelForm):
    class Meta:
        model = Ave
        exclude = []

