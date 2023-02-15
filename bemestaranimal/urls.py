from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/completar', views.cadastro_tutor, name='completar_cadastro'),
    path('area-tutor/', views.area_tutor, name='area_tutor'),

    #animal
    path('animal/cadastrar', views.cadastrar_animal, name='cadastrar_animal'),
    path('animal/', views.listar_animal, name='listar_animal'),
    path('animal/editar/<id>', views.editar_animal, name='editar_animal'),
    path('animal/deletar/<id>', views.deletar_animal, name='deletar_animal'),

    #token
    path('resgatar-cupom', views.resgatar_cupom, name='resgatar_cupom'),

    #catalogo
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/<id>/entrevista-previa', views.entrevistaAdocao, name='entrevista_adocao'),
]
