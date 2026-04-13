from django.db import models

# --- REQUISITOS DE LOCALIDADE E ESTRUTURA ---

class UF(models.Model):
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla

class Cidade(models.Model): # RF12
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, related_name='cidades')

    def __str__(self):
        return f"{self.nome} - {self.uf.sigla}"

class AreaSaber(models.Model): # RF04
    nome = models.CharField(max_length=100) # Ex: Biológicas, Exatas

    def __str__(self):
        return self.nome

class InstituicaoEnsino(models.Model): # RF03
    nome = models.CharField(max_length=150)
    site = models.URLField(blank=True, null=True)
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Turno(models.Model): # RF11
    nome = models.CharField(max_length=50) # Ex: matutino, vespertino

    def __str__(self):
        return self.nome

# --- REQUISITOS DE PESSOAS E OCUPAÇÃO (COM HERANÇA) ---

class Ocupacao(models.Model): # RF02
    nome = models.CharField(max_length=100) # Ex: Professor, estudante

    def __str__(self):
        return self.nome

class PessoaBase(models.Model):
    """Classe abstrata para cumprir o requisito 3: Implementar herança """
    nome = models.CharField(max_length=150)
    pai = models.CharField(max_length=150, blank=True, null=True)
    mae = models.CharField(max_length=150, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nasc = models.DateField()
    email = models.EmailField()

    class Meta:
        abstract = True

class Pessoa(PessoaBase): # RF01
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, related_name='pessoas')

    def __str__(self):
        return self.nome

# --- REQUISITOS ACADÊMICOS ---

class Curso(models.Model): # RF05
    nome = models.CharField(max_length=150)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.SET_NULL, null=True, related_name='cursos')
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nome

class Disciplina(models.Model): # RF07
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class CursoDisciplina(models.Model): # RF14
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas_curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    periodo = models.IntegerField() # Ex: 1 para 1º semestre

class Turma(models.Model): # RF06
    nome = models.CharField(max_length=50) # Ex: Info A, Info B
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nome

class Matricula(models.Model): # RF08
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='matriculas')
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, related_name='alunos')
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

# --- REQUISITOS DE AVALIAÇÃO E ROTINA ---

class AvaliacaoTipo(models.Model): # RF15
    nome = models.CharField(max_length=50) # Ex: Prova, trabalho

    def __str__(self):
        return self.nome

class Avaliacao(models.Model): # RF09
    descricao = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='avaliacoes')
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.descricao

class Frequencia(models.Model): # RF10
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='frequencias')
    numero_faltas = models.IntegerField()

class Ocorrencia(models.Model): # RF13
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

# --- NOVOS MODELOS ADICIONADOS ---

class Nota(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Valor da Nota")
    
    def __str__(self):
        return str(self.valor)

class Sala(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome/Número da Sala")
    capacidade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título do Evento")
    data_evento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo