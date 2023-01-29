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
                    animal = animal_form.save(commit=False)
                    v_especie = especie_form.save(commit=False)
                    especie = Especie.objects.get_or_create(nome_especie=v_especie.nome_especie)
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
    especie = Especie.objects.get(id=animal.especie_id)
    animal_form = Form_Animal(instance=animal)
    especie_form = Form_Especie(instance=especie)
    if request.method == "POST":
        especie_form = Form_Especie(request.POST, instance=especie)
        animal_form = Form_Animal(request.POST, instance=animal)
        if animal_form.is_valid() and especie_form.is_valid():
            animal_form.save(commit=False)
            try:
                Animal.objects.get(especie_id=especie.id)
                one = True
            except:
                one = False
            try:
                especie_nova = especie_form.save(commit=False)
                especie_antiga = Especie.objects.get(nome_especie=especie_nova)
                if especie_antiga:
                    animal.especie = especie_antiga
            except:  
                especie_nova = especie_form.save(commit=False)
                nova = Especie.objects.create(nome_especie=especie_nova.nome_especie)
                animal.especie = nova
            animal.save()
            if one and request.POST['nome_especie'] != especie.nome_especie:
                print(request.POST['nome_especie'])
                print(especie)
                especie.delete()
        return redirect('Cadastrar animal')               
    context = {
        'animal':animal,
        'animal_form': animal_form,
        'especie_form': especie_form,
    }
    return render(request, 'pensando/animal_editar.html', context)

def deletar_animal(request, id):
    animal = Animal.objects.get(id=id)
    animal.delete()
    return redirect('Cadastrar animal')

def cadastrar_errante(request):
    errante_form = Form_Errante()
    especie_form = Form_Especie()

    context = {
        'errante_form': errante_form,
        'especie_form': especie_form
    }
    if request.method == "POST":
        errante_form = Form_Errante(request.POST)
        especie_form = Form_Especie(request.POST)
        if errante_form.is_valid():
            if especie_form.is_valid():
                errante = errante_form.save(commit=False)
                try:
                    n_especie = especie_form.save(commit=False)
                    especie = Especie.objects.get(nome_especie=n_especie)
                    if especie:
                        errante.especie = especie
                except:      
                    especie = especie_form.save()
                    errante.especie = especie
                errante.save()

                return redirect('index')
    context = {
        'errante_form': errante_form,
        'especie_form': especie_form
    }
    return render(request, 'pensando/animal-errante-cadastro.html', context)