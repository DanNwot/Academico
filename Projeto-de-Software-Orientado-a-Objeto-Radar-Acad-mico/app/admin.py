from django.contrib import admin
from .models import *

# --- CONFIGURAÇÃO DE INLINES  ---

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1 # Requisito i: Ocupação e pessoas [cite: 13]

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1 # Requisito ii: Instituição e cursos [cite: 14] e iii: Área do saber e cursos [cite: 15]

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1 # Requisito iv: Cursos e disciplinas [cite: 16]

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1 # Requisito v: Disciplinas e avaliações [cite: 17]

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1 # Requisito vi: Turmas e alunos (via matrícula) [cite: 18]

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1 # Requisito vii: UF e cidades 

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1 # Requisito ix: Estudantes, disciplinas, avaliações, frequência [cite: 20]


# --- REGISTRO DOS MODELOS COM SEUS INLINES ---

@admin.register(UF)
class UFAdmin(admin.ModelAdmin):
    inlines = [CidadeInline] # 

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline] # [cite: 13]

@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline] # [cite: 14]

@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInline] # [cite: 15]

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline] # [cite: 16]

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline] # [cite: 17]

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline] # [cite: 18]

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    # Agrupando inlines para ter a visão completa do estudante [cite: 20]
    inlines = [MatriculaInline, FrequenciaInline]
    list_display = ('nome', 'cpf', 'ocupacao', 'email')
    search_fields = ('nome', 'cpf')

# Registrando os modelos simples restantes
admin.site.register(Cidade)
admin.site.register(Turno)
admin.site.register(AvaliacaoTipo)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)