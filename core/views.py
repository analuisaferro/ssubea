from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def cadastro(request):
    #TESTE
    try:
        animais = Animal.objects.filter(tutor=request.user.id)
        print(animais)
    except:
        pass
            #considerando que o local já é cadastrado quando o usuário é cadastrado
    animal_form = Form_Animal(initial={'tutor':Tutor.objects.get(user=request.user).id})
    if request.method == "POST":
        animal_form = Form_Animal(request.POST)
        if animal_form.is_valid():
            print('entrei')
            animal_form.save()
            animal_form = Form_Animal(initial={'tutor':Tutor.objects.get(user=request.user).id})
            print(request.user)
    context = {
        'animal_form': animal_form,
    }
    return render(request, 'pensando/animal_cadastro.html', context)
    

