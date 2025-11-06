from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome_completo = models.CharField(max_length=100)
    endereco = models.CharField(max_length=250)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Paciente: {self.nome_completo} - {self.email}"
    
class Atendente(models.Model):
    nome_completo = models.CharField(max_length=100)
    endereco = models.CharField(max_length=250)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    usuario = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Atendente: {self.nome_completo} - {self.email}"
    
    
class Medico(models.Model):
    nome_completo = models.CharField(max_length=100)
    endereco = models.CharField(max_length=250)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, help_text='Informe a unidade Federativa', verbose_name='Unidade Federativa')
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    especialidade = models.CharField(max_length=200)
    usuario = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Medico: {self.nome_completo} - {self.email}"

class Sintomas(models.Model):
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descricao
    
    
class Consultas(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete=models.PROTECT)
    atendente = models.ForeignKey(Atendente,on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico,on_delete=models.PROTECT)
    data_agendamento = models.DateTimeField(auto_now_add=True)
    data_consulta = models.DateTimeField()
    relato_paciente = models.TextField(blank=True)
    sintomas = models.ManyToManyField(Sintomas, blank=True)
    laudo = models.TextField(blank=True)
    medicacao = models.CharField(max_length=100, blank=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Data da consulta: {self.data_consulta} - {self.paciente}"