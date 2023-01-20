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
    #exibir os animais já cadastrados por aquele tutor
    tutor = Tutor.objects.get(user=request.user.id)
    print(tutor.nome)
    try:
        animais = Animal.objects.filter(tutor=tutor)
        aves = Ave.objects.filter(animal__tutor=tutor)
        for ave in aves:
            print(ave)
    except:
        animais = []
        aves = []
    animal_form = Form_Animal(initial={'tutor':Tutor.objects.get(user=request.user).id})
    ave_form = Form_Ave()
    if request.method == "POST":
        animal_form = Form_Animal(request.POST)
        if animal_form.is_valid():
            #se for cadastrar dnv os tipos ele não funciona, seria melhor pegar por outra coisa
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
    context = {
        'animal_form': animal_form,
        'ave_form':ave_form,
        'animais':animais,
        'aves': aves
    }
    return render(request, 'pensando/animal_cadastro.html', context)
    

