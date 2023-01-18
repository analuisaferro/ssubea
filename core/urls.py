

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastro, name='Cadastrar Animal')
]
