from django import forms
from .models import (
    Turma, Curso, Pessoa, InstituicaoEnsino, Disciplina, 
    Cidade, Matricula, Frequencia, AreaSaber, Ocupacao, 
    Ocorrencia, Avaliacao, Nota, Sala, Evento
)

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = InstituicaoEnsino
        fields = '__all__'

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'

class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = '__all__'

class AreaSaberForm(forms.ModelForm):
    class Meta:
        model = AreaSaber
        fields = '__all__'

class OcupacaoForm(forms.ModelForm):
    class Meta:
        model = Ocupacao
        fields = '__all__'

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = '__all__'

# --- NOVOS FORMS QUE ESTAVAM CAUSANDO O ERRO DE IMPORTAÇÃO ---
class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = '__all__'

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'