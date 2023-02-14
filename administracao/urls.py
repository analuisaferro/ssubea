from django.urls import path
from . import views

urlpatterns = [

    #errante
    path('animal/cadastrar-errante', views.cadastrar_errante, name='cadastrar_errante'),
    path('animal/listar-errante', views.listar_errante, name='listar_errantes'),

    #tutor
    path('tutor/', views.listar_tutor, name='listar_tutor'),
    path('tutor/<tutor_id>/animais/', views.listar_animal_tutor, name='listar_animais_tutor'),
    path('tutor/<tutor_id>/animais/<animal_id>', views.cad_infos_extras, name='cadastrar_info'),

    #catalogo
    path('catalogo/cadastrar', views.cad_catalogo_animal, name='cadastrar_catalogo'),
    path('entrevista-previa/', views.listar_entrevistas, name='listar_entrevistas'),
    path('entrevista-previa/<id>', views.questionario, name='questionario'),

    # path desativar animal do catalogo

    #token
    path('adm/gerar-token', views.gerarToken, name='gerar_token'),
    path('adm/descontar-token', views.descontarToken, name='descontar_token'),

    #adm
    path('administrativo/', views.administrativo, name='administrativo'),
]



