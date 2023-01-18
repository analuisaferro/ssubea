from django.shortcuts import render
from django.db.models import Count
from .models import *
from .forms import *

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def cadastro(request):
    #considerando que o local já é cadastrado quando o usuário é cadastrado
    animal_form = Form_Animal()

    # if request.method == "POST":
    #     if animal_form.is_valid():

    context = {
        'animal_form': animal_form,
    }
    return render(request, 'pensando/animal_cadastro.html', context)
    
