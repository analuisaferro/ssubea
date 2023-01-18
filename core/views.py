from django.shortcuts import render
from django.db.models import Count
from .models import *

# Create your views here.
def index(request):
    
    return render(request, 'index.html')
