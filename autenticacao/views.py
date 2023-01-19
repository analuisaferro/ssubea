from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def login_view(request):
    return render(request, 'adm/login.html')

def cadastro_user(request):
    form_tutor = Form_Tutor()
    if request.method == "POST":
        form_tutor = Form_Tutor(request.POST)
        if form_tutor.is_valid():
            
            if request.POST['password'] == request.POST['password2']:
                
                try:

                    user = User.objects.create_user(username=request.POST['email'], email=request.POST['email'], password=request.POST['password'])
                    print('toaqui')
                    user.first_name = request.POST['nome']
                    # salvando pra mais tarde::
                    userid = user.id
                    user.save()
                    form_tutor.save()
                    tutor = Tutor.objects.get(email=request.POST['email'])
                    tutor.user_id = userid
                    tutor.save()
                except Exception as e:
                    #acredito que só cai aqui se já existir
                    messages.error(request, 'Email de usuário já cadastrado')
            else:
                #as senhas não se coincidem
                messages.error(request, 'As senhas digitadas não se coincidem')
                pass
            
    context = {
        'form_tutor': form_tutor,
    }
    return render(request, 'adm/cadastro.html', context)