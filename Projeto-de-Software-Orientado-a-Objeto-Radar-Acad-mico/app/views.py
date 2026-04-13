from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    TurmaForm, CursoForm, PessoaForm, InstituicaoForm, DisciplinaForm, 
    CidadeForm, MatriculaForm, FrequenciaForm, AreaSaberForm, 
    OcupacaoForm, OcorrenciaForm, AvaliacaoForm, NotaForm, SalaForm, EventoForm
)
from .models import (
    Curso, Pessoa, InstituicaoEnsino, Cidade,
    AreaSaber, Ocupacao, Turno, Turma,
    Disciplina, Frequencia, Ocorrencia, Matricula,
    Avaliacao, Nota, Sala, Evento
)

def home(request):
    return render(request, 'app/home.html')

def lista_generica(request, model, template, context_name):
    objetos = model.objects.all()
    return render(request, template, {context_name: objetos})

def turno_list(request): return lista_generica(request, Turno, 'app/turno_list.html', 'turnos')

# --- CRUD TURMA ---
def turma_list(request): return lista_generica(request, Turma, 'app/turma_list.html', 'turmas')
def turma_criar(request):
    form = TurmaForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('turma_list')
    return render(request, 'app/turma_form.html', {'form': form, 'acao': 'Nova Turma'})
def turma_editar(request, id):
    turma = get_object_or_404(Turma, id=id)
    form = TurmaForm(request.POST or None, instance=turma)
    if form.is_valid(): form.save(); return redirect('turma_list')
    return render(request, 'app/turma_form.html', {'form': form, 'acao': 'Editar Turma'})
def turma_excluir(request, id):
    turma = get_object_or_404(Turma, id=id)
    if request.method == 'POST': turma.delete(); return redirect('turma_list')
    return render(request, 'app/turma_confirm_delete.html', {'obj': turma})

# --- CRUD CURSO ---
def curso_list(request): return lista_generica(request, Curso, 'app/curso_list.html', 'cursos')
def curso_criar(request):
    form = CursoForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('curso_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Novo Curso'})
def curso_editar(request, id):
    obj = get_object_or_404(Curso, id=id); form = CursoForm(request.POST or None, instance=obj)
    if form.is_valid(): form.save(); return redirect('curso_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Editar Curso'})
def curso_excluir(request, id):
    obj = get_object_or_404(Curso, id=id)
    if request.method == 'POST': obj.delete(); return redirect('curso_list')
    return render(request, 'app/delete_universal.html', {'obj': obj})

# --- CRUD PESSOA ---
def pessoa_list(request): return lista_generica(request, Pessoa, 'app/pessoa_list.html', 'pessoas')
def pessoa_criar(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('pessoa_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Nova Pessoa'})
def pessoa_editar(request, id):
    obj = get_object_or_404(Pessoa, id=id); form = PessoaForm(request.POST or None, instance=obj)
    if form.is_valid(): form.save(); return redirect('pessoa_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Editar Pessoa'})
def pessoa_excluir(request, id):
    obj = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST': obj.delete(); return redirect('pessoa_list')
    return render(request, 'app/delete_universal.html', {'obj': obj})

# --- CRUD INSTITUIÇÃO ---
def instituicao_list(request): return lista_generica(request, InstituicaoEnsino, 'app/instituicao_list.html', 'instituicoes')
def instituicao_criar(request):
    form = InstituicaoForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('instituicao_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Nova Instituição'})
def instituicao_editar(request, id):
    obj = get_object_or_404(InstituicaoEnsino, id=id); form = InstituicaoForm(request.POST or None, instance=obj)
    if form.is_valid(): form.save(); return redirect('instituicao_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Editar Instituição'})
def instituicao_excluir(request, id):
    obj = get_object_or_404(InstituicaoEnsino, id=id)
    if request.method == 'POST': obj.delete(); return redirect('instituicao_list')
    return render(request, 'app/delete_universal.html', {'obj': obj})

# --- CRUD DISCIPLINA ---
def disciplina_list(request): return lista_generica(request, Disciplina, 'app/disciplina_list.html', 'disciplinas')
def disciplina_criar(request):
    form = DisciplinaForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('disciplina_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Nova Disciplina'})
def disciplina_editar(request, id):
    obj = get_object_or_404(Disciplina, id=id); form = DisciplinaForm(request.POST or None, instance=obj)
    if form.is_valid(): form.save(); return redirect('disciplina_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Editar Disciplina'})
def disciplina_excluir(request, id):
    obj = get_object_or_404(Disciplina, id=id)
    if request.method == 'POST': obj.delete(); return redirect('disciplina_list')
    return render(request, 'app/delete_universal.html', {'obj': obj})

# --- CRUD CIDADE ---
def cidade_list(request): return lista_generica(request, Cidade, 'app/cidade_list.html', 'cidades')
def cidade_criar(request):
    form = CidadeForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('cidade_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Nova Cidade'})
def cidade_editar(request, id):
    obj = get_object_or_404(Cidade, id=id); form = CidadeForm(request.POST or None, instance=obj)
    if form.is_valid(): form.save(); return redirect('cidade_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Editar Cidade'})
def cidade_excluir(request, id):
    obj = get_object_or_404(Cidade, id=id)
    if request.method == 'POST': obj.delete(); return redirect('cidade_list')
    return render(request, 'app/delete_universal.html', {'obj': obj})

# --- CRUD MATRÍCULAS ---
def matricula_list(request): return lista_generica(request, Matricula, 'app/matricula_list.html', 'matriculas')
def matricula_criar(request):
    form = MatriculaForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('matricula_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Nova Matrícula'})
def matricula_editar(request, id):
    obj = get_object_or_404(Matricula, id=id); form = MatriculaForm(request.POST or None, instance=obj)
    if form.is_valid(): form.save(); return redirect('matricula_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Editar Matrícula'})
def matricula_excluir(request, id):
    obj = get_object_or_404(Matricula, id=id)
    if request.method == 'POST': obj.delete(); return redirect('matricula_list')
    return render(request, 'app/delete_universal.html', {'obj': obj})

# --- CRUD FREQUÊNCIAS ---
def frequencia_list(request): return lista_generica(request, Frequencia, 'app/frequencia_list.html', 'frequencias')
def frequencia_criar(request):
    form = FrequenciaForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('frequencia_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Lançar Frequência'})
def frequencia_editar(request, id):
    obj = get_object_or_404(Frequencia, id=id); form = FrequenciaForm(request.POST or None, instance=obj)
    if form.is_valid(): form.save(); return redirect('frequencia_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Editar Frequência'})
def frequencia_excluir(request, id):
    obj = get_object_or_404(Frequencia, id=id)
    if request.method == 'POST': obj.delete(); return redirect('frequencia_list')
    return render(request, 'app/delete_universal.html', {'obj': obj})

# --- CRUD ÁREAS DO SABER ---
def area_saber_list(request): return lista_generica(request, AreaSaber, 'app/area_saber_list.html', 'areas')
def area_saber_criar(request):
    form = AreaSaberForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('area_saber_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Nova Área do Saber'})

# --- CRUD OCUPAÇÕES ---
def ocupacao_list(request): return lista_generica(request, Ocupacao, 'app/ocupacao_list.html', 'ocupacoes')
def ocupacao_criar(request):
    form = OcupacaoForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('ocupacao_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Nova Ocupação'})

# --- CRUD OCORRÊNCIAS ---
def ocorrencia_list(request): return lista_generica(request, Ocorrencia, 'app/ocorrencia_list.html', 'ocorrencias')
def ocorrencia_criar(request):
    form = OcorrenciaForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('ocorrencia_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Nova Ocorrência'})

# --- NOVAS VIEWS (Avaliações, Notas, Salas e Eventos) ---
def avaliacao_list(request): return lista_generica(request, Avaliacao, 'app/avaliacao_list.html', 'avaliacoes')
def avaliacao_criar(request):
    form = AvaliacaoForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('avaliacao_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Nova Avaliação'})

def nota_list(request): return lista_generica(request, Nota, 'app/nota_list.html', 'notas')
def nota_criar(request):
    form = NotaForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('nota_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Lançar Nota'})

def sala_list(request): return lista_generica(request, Sala, 'app/sala_list.html', 'salas')
def sala_criar(request):
    form = SalaForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('sala_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Nova Sala'})

def evento_list(request): return lista_generica(request, Evento, 'app/evento_list.html', 'eventos')
def evento_criar(request):
    form = EventoForm(request.POST or None)
    if form.is_valid(): form.save(); return redirect('evento_list')
    return render(request, 'app/form_universal.html', {'form': form, 'acao': 'Novo Evento'})