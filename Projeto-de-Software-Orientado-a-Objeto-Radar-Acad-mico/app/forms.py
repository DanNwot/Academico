from django import forms
from .models import Turma, Curso, Pessoa, InstituicaoEnsino, Disciplina, Cidade, Matricula, Frequencia

# Classe Base Inteligente: Aplica o Dark Mode em TODOS os campos automaticamente
class BaseDarkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control bg-dark text-white border-secondary'

# Agora criamos os formulários com apenas 3 linhas cada!
class TurmaForm(BaseDarkForm):
    class Meta: model = Turma; fields = '__all__'

class CursoForm(BaseDarkForm):
    class Meta: model = Curso; fields = '__all__'

class PessoaForm(BaseDarkForm):
    class Meta: model = Pessoa; fields = '__all__'

class InstituicaoForm(BaseDarkForm):
    class Meta: model = InstituicaoEnsino; fields = '__all__' # CORRIGIDO AQUI

class DisciplinaForm(BaseDarkForm):
    class Meta: model = Disciplina; fields = '__all__'

class CidadeForm(BaseDarkForm):
    class Meta: model = Cidade; fields = '__all__'

class MatriculaForm(BaseDarkForm):
    class Meta: 
        model = Matricula
        fields = '__all__'
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_previsao_termino': forms.DateInput(attrs={'type': 'date'}),
        }

class FrequenciaForm(BaseDarkForm):
    class Meta:
        model = Frequencia
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            }