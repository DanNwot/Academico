from django.shortcuts import render

from .models import (
    Curso, Pessoa, InstituicaoEnsino, Cidade,
    AreaSaber, Ocupacao, Turno, Turma,
    Disciplina, Frequencia, Ocorrencia
)


def home(request):
    return render(request, 'app/home.html')


# Função genérica para evitar repetição
def lista_generica(request, model, template, context_name):
    objetos = model.objects.all()
    return render(request, template, {context_name: objetos})


def curso_list(request):
    return lista_generica(request, Curso, 'app/curso_list.html', 'cursos')


def pessoa_list(request):
    return lista_generica(request, Pessoa, 'app/pessoa_list.html', 'pessoas')


def instituicao_list(request):
    return lista_generica(request, InstituicaoEnsino, 'app/instituicao_list.html', 'instituicoes')


def cidade_list(request):
    return lista_generica(request, Cidade, 'app/cidade_list.html', 'cidades')


def area_saber_list(request):
    return lista_generica(request, AreaSaber, 'app/area_saber_list.html', 'areas')


def ocupacao_list(request):
    return lista_generica(request, Ocupacao, 'app/ocupacao_list.html', 'ocupacoes')


def turno_list(request):
    return lista_generica(request, Turno, 'app/turno_list.html', 'turnos')


def turma_list(request):
    return lista_generica(request, Turma, 'app/turma_list.html', 'turmas')


def disciplina_list(request):
    return lista_generica(request, Disciplina, 'app/disciplina_list.html', 'disciplinas')


def frequencia_list(request):
    return lista_generica(request, Frequencia, 'app/frequencia_list.html', 'frequencias')


def ocorrencia_list(request):
    return lista_generica(request, Ocorrencia, 'app/ocorrencia_list.html', 'ocorrencias')