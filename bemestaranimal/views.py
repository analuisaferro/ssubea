from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import *
from .forms import *

# Create your views here.

# def aluno_required(view_func):
#     @wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             pessoa = ''
#             aluno = ''

#             try:
#                 pessoa = Pessoa.objects.get(user=request.user)
#             except Exception as e:
#                 return redirect("cadastrar_usuario")

#             try:
#                 aluno = Aluno.objects.get(pessoa=pessoa)
#             except Aluno.DoesNotExist:
#                 return redirect("cadastrar_aluno")

#         else:
#             return redirect(settings.LOGIN_URL)
        
#         return view_func(request, *args, **kwargs)
#     return wrapper

def cadastro_tutor(request):
    if request.user.is_authenticated:
        try:
            pessoa = Pessoa.objects.get(user_id=request.user.id)
            if pessoa:
                pass
        except:
            return redirect('cadastrar_usuario')
        try:
            tutor = Tutor.objects.get(pessoa_id=pessoa.id)
            verify = True
        except:
            verify = False

        if not verify:
            print(pessoa)
            form_tutor = Form_Tutor(initial={'pessoa':pessoa})
        else:
            return redirect('index')
    else:
        return redirect('cadastrar_usuario')
    if request.method == "POST":
        form_tutor = Form_Tutor(request.POST)
        if form_tutor.is_valid():
            form_tutor.save()
            return redirect('index')
    context={
        'form_tutor':form_tutor
    }
    return render(request, 'autenticacao/completar-cadastro.html', context)



def index(request):
    return render(request, 'index.html')

@login_required
def cadastrar_animal(request):
    try:
        pessoa = Pessoa.objects.get(user_id=request.user.id)
        tutor = Tutor.objects.get(pessoa_id=pessoa.id)
        animal_form = Form_Animal(initial={'tutor':tutor})
    except:
        messages.error(request, 'Você não é cadastrado como tutor!')
        return redirect('completar_cadastro')
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
            animal_form = Form_Animal(initial={'tutor':tutor})
            especie_form = Form_Especie()


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
        return redirect('cadastrar_animal')               
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
    return redirect('cadastrar_animal')

def catalogo(request):
    catalogo = Catalogo.objects.all()
    context = {
        'catalogo':catalogo
    }
    return render(request, 'catalogo/animal-catalogo.html', context)


def entrevistaAdocao(request, id):
    animal = Catalogo.objects.get(pk=id)
    entrevistaPrevia_Form = Form_EntrevistaPrevia(initial={'animal':animal})
    if request.method == "POST":
        entrevistaPrevia_Form = Form_EntrevistaPrevia(request.POST)
        if entrevistaPrevia_Form.is_valid():
            entrevistaPrevia_Form.save()
            messages.success(request, 'Uma orientação?')
            return redirect('index')
    context = {
        'entrevistaPrevia_Form': entrevistaPrevia_Form,
        'adocao':animal
    }
    return render(request, 'catalogo/entrevista.html', context)
    



#quantidade de animais castrados e não castrados
# vacinados (mas não pede essa informação no usuário, só na hora de cadastrar as informações extras)