

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animal/cadastrar', views.cadastrar_animal, name='Cadastrar animal'),
    path('animal/editar/<id>', views.editar_animal, name='Editar animal'),
    path('animal/deletar/<id>', views.deletar_animal, name='Deletar animal'),
    path('animal/cadastrar-errante', views.cadastrar_errante, name='Cadastrar errante'),
    path('tutor/', views.listar_tutor, name='listar tutor'),
    path('tutor/<tutor_id>/animais/', views.listar_animal_tutor, name='listar animais tutor'),
    path('tutor/<tutor_id>/animais/<animal_id>', views.cad_info_extra, name='cadastrar info extra')

]
