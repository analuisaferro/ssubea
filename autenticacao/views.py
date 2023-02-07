from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context = {
                'error': True,
            }
    return render(request, 'adm/login.html', context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/')

def cadastro_user(request):
    form_pessoa = Form_Pessoa()
    if request.method == "POST":
        form_pessoa = Form_Pessoa(request.POST)
        if form_pessoa.is_valid():
            if request.POST['password'] == request.POST['password2']:
                if len(request.POST['password']) >= 8:
                    try:
                        user = User.objects.create_user(username=request.POST['email'], email=request.POST['email'], password=request.POST['password'])
                        user.first_name = request.POST['nome']
                        # salvando pra mais tarde::
                        userid = user.id
                        user.save()
                        pessoa = form_pessoa.save(commit=False)
                        pessoa.user_id = userid
                        pessoa.save()
                        messages.success(request, 'Usuário cadastrado com sucesso!')
                        return redirect('/login')
                    except Exception as e:
                        #acredito que só cai aqui se já existir
                        messages.error(request, 'Email de usuário já cadastrado')
                messages.error(request, 'A senha deve possuir pelo menos 9 caracteres')
            else:
                #as senhas não se coincidem
                messages.error(request, 'As senhas digitadas não se coincidem')
    context = {
        'form_pessoa': form_pessoa,
    }
    return render(request, 'adm/cadastro.html', context)