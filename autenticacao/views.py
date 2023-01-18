from django.shortcuts import render
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
                user = User.objects.create_user(request.POST['email'], request.POST['email'], request.POST['password'])
        
    context = {
        'form_tutor': form_tutor,
    }
    return render(request, 'adm/cadastro.html', context)