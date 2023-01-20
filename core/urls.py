

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar-animal/', views.cadastro, name='Cadastrar animal')
]
