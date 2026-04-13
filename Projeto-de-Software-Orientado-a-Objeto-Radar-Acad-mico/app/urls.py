from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # --- LISTAGENS BASE ---
    path('areas/', views.area_saber_list, name='area_saber_list'),
    path('ocupacoes/', views.ocupacao_list, name='ocupacao_list'),
    path('turnos/', views.turno_list, name='turno_list'),

    # --- CRUD CIDADES ---
    path('cidades/', views.cidade_list, name='cidade_list'),
    path('cidades/nova/', views.cidade_criar, name='cidade_criar'),
    path('cidades/editar/<int:id>/', views.cidade_editar, name='cidade_editar'),
    path('cidades/excluir/<int:id>/', views.cidade_excluir, name='cidade_excluir'),

    # --- CRUD INSTITUIÇÕES ---
    path('instituicoes/', views.instituicao_list, name='instituicao_list'),
    path('instituicoes/nova/', views.instituicao_criar, name='instituicao_criar'),
    path('instituicoes/editar/<int:id>/', views.instituicao_editar, name='instituicao_editar'),
    path('instituicoes/excluir/<int:id>/', views.instituicao_excluir, name='instituicao_excluir'),

    # --- CRUD CURSOS ---
    path('cursos/', views.curso_list, name='curso_list'),
    path('cursos/novo/', views.curso_criar, name='curso_criar'),
    path('cursos/editar/<int:id>/', views.curso_editar, name='curso_editar'),
    path('cursos/excluir/<int:id>/', views.curso_excluir, name='curso_excluir'),

    # --- CRUD TURMAS ---
    path('turmas/', views.turma_list, name='turma_list'),
    path('turmas/nova/', views.turma_criar, name='turma_criar'),
    path('turmas/editar/<int:id>/', views.turma_editar, name='turma_editar'),
    path('turmas/excluir/<int:id>/', views.turma_excluir, name='turma_excluir'),

    # --- CRUD DISCIPLINAS ---
    path('disciplinas/', views.disciplina_list, name='disciplina_list'),
    path('disciplinas/nova/', views.disciplina_criar, name='disciplina_criar'),
    path('disciplinas/editar/<int:id>/', views.disciplina_editar, name='disciplina_editar'),
    path('disciplinas/excluir/<int:id>/', views.disciplina_excluir, name='disciplina_excluir'),

    # --- CRUD PESSOAS ---
    path('pessoas/', views.pessoa_list, name='pessoa_list'),
    path('pessoas/nova/', views.pessoa_criar, name='pessoa_criar'),
    path('pessoas/editar/<int:id>/', views.pessoa_editar, name='pessoa_editar'),
    path('pessoas/excluir/<int:id>/', views.pessoa_excluir, name='pessoa_excluir'),

    # --- CRUD MATRÍCULAS ---
    path('matriculas/', views.matricula_list, name='matricula_list'),
    path('matriculas/nova/', views.matricula_criar, name='matricula_criar'),
    path('matriculas/editar/<int:id>/', views.matricula_editar, name='matricula_editar'),
    path('matriculas/excluir/<int:id>/', views.matricula_excluir, name='matricula_excluir'),

    # --- CRUD FREQUÊNCIAS ---
    path('frequencias/', views.frequencia_list, name='frequencia_list'),
    path('frequencias/nova/', views.frequencia_criar, name='frequencia_criar'),
    path('frequencias/editar/<int:id>/', views.frequencia_editar, name='frequencia_editar'),
    path('frequencias/excluir/<int:id>/', views.frequencia_excluir, name='frequencia_excluir'),

    # --- OUTRAS LISTAGENS ---
    path('ocorrencias/', views.ocorrencia_list, name='ocorrencia_list'),
]