

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animal/cadastrar', views.cadastrar_animal, name='cadastrar animal'),
    path('animal/editar/<id>', views.editar_animal, name='editar animal'),
    path('animal/deletar/<id>', views.deletar_animal, name='deletar animal'),
    path('animal/cadastrar-errante', views.cadastrar_errante, name='cadastrar errante'),
    path('tutor/', views.listar_tutor, name='listar tutor'),
    path('tutor/<tutor_id>/animais/', views.listar_animal_tutor, name='listar animais tutor'),
    path('tutor/<tutor_id>/animais/<animal_id>', views.cad_infos_extras, name='cadastrar info'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/cadastrar', views.cad_catalogo_animal, name='cadastrar catalogo'),
    path('catalogo/<id>/entrevista-previa', views.entrevistaAdocao, name='entrevista adocao'),
    path('teste/', views.resgatarToken, name='yoo'),
    path('adm/descontar-token', views.descontarToken, name='descontar token'),
]
