from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def cadastrar_animal(request):

    animal_form = Form_Animal(initial={'tutor':Tutor.objects.get(user=request.user).id})
    ave_form = Form_Ave()
    if request.method == "POST":
        animal_form = Form_Animal(request.POST)
        if animal_form.is_valid():
            if request.POST['tipo'] == '1':
                ave_form = Form_Ave(request.POST)
                if ave_form.is_valid():
                    animal = animal_form.save()
                    ave=ave_form.save(commit=False)
                    ave.animal_id=animal.id
                    ave.save()
                    animal_form = Form_Animal(initial={'tutor':Tutor.objects.get(user=request.user).id})
            else:
                animal_form.save()
                animal_form = Form_Animal(initial={'tutor':Tutor.objects.get(user=request.user).id})

    tutor = Tutor.objects.get(user=request.user.id)
    try:
        animais = Animal.objects.filter(tutor=tutor)
        aves = Ave.objects.filter(animal__tutor=tutor)
    except:
        animais = []
        aves = []
    context = {
        'animal_form': animal_form,
        'ave_form':ave_form,
        'animais':animais,
        'aves': aves
    }
    return render(request, 'pensando/animal_cadastro.html', context)
    
def editar_animal(request, id):
    is_ave = False
    animal = Animal.objects.get(id=id)
    animal_form = Form_Animal(instance=animal)
    try:
        ave = Ave.objects.get(animal_id=id)
        if ave:
            ave_form = Form_Ave(instance=ave)
            is_ave = True
    except:
        ave_form = Form_Ave()
    if request.method == "POST":
        animal_form = Form_Animal(request.POST, instance=animal)
        if animal_form.is_valid():
            if request.POST['tipo'] == '1' and is_ave:
                print("o 1 está selecionado e já tinha um animal cadastrado como ave")
                ave_form = Form_Ave(request.POST, instance=ave)
                if ave_form.is_valid():
                    ave_form.save()
                    animal_form.save()
            elif request.POST['tipo'] == '1' and not is_ave:
                print("o 1 está selecionado e não tinha um animal cadastrado como ave")
                ave_form = Form_Ave(request.POST)
                if ave_form.is_valid():
                    animal = animal_form.save()
                    ave=ave_form.save(commit=False)
                    ave.animal_id=animal.id
                    ave.save()
                    animal_form = Form_Animal(initial={'tutor':Tutor.objects.get(user=request.user).id})
            else:
                if ave:
                    print("o 1 não está selecionado e tinha um animal cadastrado como ave")
                    ave.delete()
                animal_form.save()
            return redirect('Cadastrar animal')
    context = {
        'animal_form': animal_form,
        'ave_form': ave_form
    }
    return render(request, 'pensando/animal_editar.html', context)

def deletar_animal(request, id):
    animal = Animal.objects.get(id=id)
    animal.delete()
    return render(request, 'pensando/animal_cadastro.html')