

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar-animal/', views.cadastrar_animal, name='Cadastrar animal'),
    path('editar-animal/<id>', views.editar_animal, name='Editar animal'),
    path('deletar-animal/<id>', views.deletar_animal, name='Deletar animal'),
    path('denuncia/animal', views.cadastrar_errante, name='Cadastrar errante'),
    path('teste/', views.listar_tutor, name='listar tutor')

]
