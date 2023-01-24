from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def cadastrar_animal(request):
    animal_form = Form_Animal(initial={'tutor':Tutor.objects.get(user=request.user).id})
    especie_form = Form_Especie()
    if request.method == "POST":
        animal_form = Form_Animal(request.POST)
        especie_form = Form_Especie(request.POST)
        if animal_form.is_valid():
            if especie_form.is_valid():
                    especie = especie_form.save()
                    animal = animal_form.save(commit=False)
                    animal.especie = especie
                    animal.save()   
                    animal_form = Form_Animal(initial={'tutor':Tutor.objects.get(user=request.user).id})

    tutor = Tutor.objects.get(user=request.user.id)
    try:
        animais = Animal.objects.filter(tutor=tutor)
    except:
        animais = []
    context = {
        'animal_form': animal_form,
        'especie_form': especie_form,
        'animais':animais,
    }
    return render(request, 'pensando/animal_cadastro.html', context)
    
def editar_animal(request, id):
    animal = Animal.objects.get(id=id)
    animal_form = Form_Animal(instance=animal)
    if request.method == "POST":
        animal_form = Form_Animal(request.POST, instance=animal)
        if animal_form.is_valid():
            animal_form.save()
    context = {
        'animal_form': animal_form,
    }
    return render(request, 'pensando/animal_editar.html', context)

def deletar_animal(request, id):
    animal = Animal.objects.get(id=id)
    animal.delete()
    return render(request, 'pensando/animal_cadastro.html')