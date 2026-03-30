from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cursos/', views.curso_list, name='curso_list'),
    path('pessoas/', views.pessoa_list, name='pessoa_list'),
    path('instituicoes/', views.instituicao_list, name='instituicao_list'),
    path('cidades/', views.cidade_list, name='cidade_list'),
    path('areas/', views.area_saber_list, name='area_saber_list'),
    path('ocupacoes/', views.ocupacao_list, name='ocupacao_list'),
    path('turnos/', views.turno_list, name='turno_list'),
    
    # NOVAS ROTAS:
    path('turmas/', views.turma_list, name='turma_list'),
    path('disciplinas/', views.disciplina_list, name='disciplina_list'),
    path('frequencias/', views.frequencia_list, name='frequencia_list'),
    path('ocorrencias/', views.ocorrencia_list, name='ocorrencia_list'),
]