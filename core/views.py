from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import *
from .forms import *
from .functions import generateToken

# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required
def cadastrar_animal(request):
    try:
        animal_form = Form_Animal(initial={'tutor':Tutor.objects.get(user=request.user).id})
    except:
        messages.error(request, 'Você não é cadastrado como tutor!')
        return redirect('cadastrar usuário')
    especie_form = Form_Especie()
    if request.method == "POST":
        animal_form = Form_Animal(request.POST, request.FILES)
        especie_form = Form_Especie(request.POST)
        if animal_form.is_valid() and especie_form.is_valid():
            animal = animal_form.save(commit=False)
            v_especie = especie_form.save(commit=False)
            especie, verify = Especie.objects.get_or_create(nome_especie=v_especie.nome_especie)
            animal.especie_id = especie.id
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
    return render(request, 'tutor/animal_cadastro.html', context)

@login_required
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
            v_especie = especie_form.save(commit=False)
            especie, verify = Especie.objects.get_or_create(nome_especie=v_especie.nome_especie)
            animal.especie = especie
            animal.save()
            if one and request.POST['nome_especie'] != especie.nome_especie:
                try:
                    especie.delete()
                except:
                    pass
        return redirect('cadastrar animal')               
    context = {
        'animal':animal,
        'animal_form': animal_form,
        'especie_form': especie_form,
    }
    return render(request, 'tutor/animal_editar.html', context)

@login_required
def deletar_animal(request, id):
    animal = Animal.objects.get(pk=id)
    animal.delete()
    return redirect('cadastrar animal')

@login_required
def cadastrar_errante(request):
    errante_form = Form_Errante()
    especie_form = Form_Especie()

    context = {
        'errante_form': errante_form,
        'especie_form': especie_form
    }
    if request.method == "POST":
        errante_form = Form_Errante(request.POST, request.FILES)
        especie_form = Form_Especie(request.POST)
        if errante_form.is_valid():
            if especie_form.is_valid():
                errante = errante_form.save(commit=False)
                v_especie = especie_form.save(commit=False)
                especie, verify = Especie.objects.get_or_create(nome_especie=v_especie.nome_especie)
                errante.especie = especie
                errante.save()

                return redirect('index')
    context = {
        'errante_form': errante_form,
        'especie_form': especie_form
    }
    return render(request, 'adm/animal-errante-cadastro.html', context)

@login_required
def listar_tutor(request):
    tutores = Tutor.objects.all()
    qntd = Tutor.objects.all().count()
    context = {
        'tutores':tutores,
        'qntd':qntd
    }
    return render(request, 'adm/listar-tutores.html', context)

@login_required
def listar_animal_tutor(request, tutor_id):
    animais = Animal.objects.filter(tutor_id=tutor_id)
    tutor = Tutor.objects.get(pk=tutor_id).nome
    context = {
        'animais':animais,
        'tutor':tutor
    }
    return render(request, 'adm/listar-animais-tutor.html', context)

@login_required
def cad_infos_extras(request, tutor_id, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    try:
        info = Informacoes_Extras.objects.get(animal=animal.id)
        if info:
            info_extras_form = Form_Info_Extras(instance=info)
    except:
        info_extras_form = Form_Info_Extras(initial={'animal':Animal.objects.get(pk=animal_id).id})
    context = {
        'info_extras_form':info_extras_form,
        'animal':animal
    }
    if request.method == "POST":
        if info:
            info_extras_form = Form_Info_Extras(request.POST, instance=info)
        else:
            info_extras_form = Form_Info_Extras(request.POST)
        if info_extras_form.is_valid():
            info_extras_form.save()
    return render(request, 'adm/info-extra-cadastrar.html', context)

@login_required
def cad_catalogo_animal(request):
    animal_catalogo_form = Form_Catalogo()
    if request.method == "POST":
        animal_catalogo_form = Form_Catalogo(request.POST, request.FILES)
        if animal_catalogo_form.is_valid():
            animal_catalogo_form.save()
            messages.success(request, 'Animal cadastrado com sucesso!')
            animal_catalogo_form = Form_Catalogo()
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    context = {
        'animal_catalogo_form':animal_catalogo_form
    }
    return render(request, 'adm/animal-catalogo-cadastrar.html', context)

@login_required
def catalogo(request):
    catalogo = Catalogo.objects.all()
    context = {
        'catalogo':catalogo
    }
    return render(request, 'tutor/animal-catalogo.html', context)

@login_required
def resgatarToken(request):
    tutor = Tutor.objects.get(user=request.user)
    print(type(tutor.id))
    token = generateToken(tutor.id)
    new = TokenDesconto.objects.create(token=token)
    print(new.token)

@login_required
def descontarToken(request):
    if request.method == 'POST':
        token = request.POST['token']
        print(token)
        try:
            verify = TokenDesconto.objects.get(token=token)
        except:
            messages.error(request, 'Código promocional inválido.')
            return render(request, 'adm/descontar-token.html')
        if verify.used:
            messages.error(request, 'Código promocional já utilizado.')
        else:
            verify.used = True
            verify.save()
            messages.success(request, 'Código promocional ativado com sucesso!')
    return render(request, 'adm/descontar-token.html')
