from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models import Count
from bemestaranimal.models import *
from bemestaranimal.forms import *
from .functions import generateToken

# Create your views here.
@staff_member_required
def administrativo(request):
    return render(request, 'adm/administracao.html')

@staff_member_required
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
                messages.success(request, 'Animal cadastrado com sucesso!')
                return redirect('cadastrar_errante')
    context = {
        'errante_form': errante_form,
        'especie_form': especie_form
    }
    return render(request, 'errante/animal-errante-cadastro.html', context)

@staff_member_required
def listar_errante(request):
    errantes = Errante.objects.all()
    context = {
        'errantes':errantes
    }
    return render(request, 'errante/animal_errante.html', context)

@staff_member_required
def listar_tutor(request):
    qntd = Tutor.objects.all().count()
    tutores = Tutor.objects.annotate(num=Count('animal'))
    context = {
        'tutores':tutores,
        'qntd':qntd,
    }
    return render(request, 'adm/listar-tutores.html', context)

@staff_member_required
def listar_animal_tutor(request, tutor_id):
    animais = Animal.objects.filter(tutor_id=tutor_id)
    tutor = Tutor.objects.get(pk=tutor_id).pessoa.nome
    context = {
        'animais':animais,
        'tutor':tutor
    }
    return render(request, 'adm/listar-animais-tutor.html', context)


@staff_member_required
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

@staff_member_required
def cad_catalogo_animal(request):
    animal_form = Form_Animal()
    especie_form = Form_Especie()
    animal_catalogo_form = Form_Catalogo()
    if request.method == "POST":
        especie_form = Form_Especie(request.POST)
        animal_form = Form_Animal(request.POST, request.FILES)
        animal_catalogo_form = Form_Catalogo(request.POST)
        if animal_form.is_valid() and especie_form.is_valid():
            animal = animal_form.save(commit=False)
            v_especie = especie_form.save(commit=False)
            especie, verify = Especie.objects.get_or_create(nome_especie=v_especie.nome_especie)
            animal.especie_id = especie.id
            animal.save()
            if animal_catalogo_form.is_valid():
                animal_adocao = animal_catalogo_form.save(commit=False)
                animal_adocao.animal=animal
                animal_adocao.save()
                messages.success(request, 'Animal cadastrado com sucesso!')
                animal_form = Form_Animal()
                especie_form = Form_Especie()
                animal_catalogo_form = Form_Catalogo()
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    context = {
        'animal_catalogo_form':animal_catalogo_form,
        'especie_form':especie_form,
        'animal_form':animal_form

    }
    return render(request, 'catalogo/animal-catalogo-cadastrar.html', context)

@staff_member_required
def listar_entrevistas(request):
    estrevistas = EntrevistaPrevia.objects.all()
    context = {
        'entrevistas':estrevistas
    }
    return render(request, 'adm/listar_entrevista_previa.html', context)

@staff_member_required
def questionario(request, id):
    entrevista = EntrevistaPrevia.objects.get(pk=id)
    form_entrevista = Form_EntrevistaPrevia(instance=entrevista)
    context = {
        'entrevista':entrevista,
        'form_entrevista':form_entrevista
    }
    return render(request, 'adm/questionario.html', context)

@staff_member_required
def gerarToken(request):
    #pra conseguir só os tutores que tem animal cadastrado
    tutores = Tutor.objects.all()
    count_s = 0
    count_n = 0
    for tutor in tutores:
        if len(Animal.objects.filter(tutor=tutor))!=0:
            try:
                TokenDesconto.objects.get(tutor=tutor)
            except:
                token = generateToken(tutor.id)
                new = TokenDesconto.objects.create(token=token, tutor=tutor)
                new.save()
                count_s += 1
        else:
            count_n += 1
    context = {
        'tutor_animal':count_s,
        'tutor_s_animal':count_n
    }
    return render(request, 'adm/gerar-token.html', context)

@staff_member_required
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

@staff_member_required
def censo(request):
    animais_tutor = Animal.objects.exclude(tutor=None)
    animais_tutor.filter(castrado=True)
    errantes = Errante.objects.all().count()
    adocao = Catalogo.objects.all().count()
    tutores = Tutor.objects.all().count()
    animais = Animal.objects.all()
    castrados = [
        {'tipo': 'Castrados', 'quantidade': animais_tutor.filter(castrado=True).count()},
        {'tipo': 'Não castrados', 'quantidade': animais_tutor.filter(castrado=False).count()}
    ]
    Animais = [
        {'tipo':'Animais c/ tutor', 'quantidade':animais.exclude(tutor=None).count(), 'color':'red'},
        {'tipo':'Animais p/ adoção', 'quantidade':animais.filter(tutor=None).count(), 'color':'blue'},
        {'tipo':'Animais errantes', 'quantidade':errantes, 'color':'yellow'}


    ]
    context = {
        'castrados':castrados,
        'errantes':errantes,
        'adocao':adocao,
        'tutores':tutores,
        'animais_tutor':animais_tutor.count()
    }
    return render(request, 'adm/censo.html', context)


#quantidade de animais castrados e não castrados
# vacinados (mas não pede essa informação no usuário, só na hora de cadastrar as informações extras)