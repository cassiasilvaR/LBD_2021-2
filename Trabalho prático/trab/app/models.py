from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Escritor(models.Model):
    nome = models.CharField(max_length=50)
    area_atuacao = models.CharField(max_length=50)

#Relacionamento 1:n - Uma estante pode conter vários livros da mesma categoria
class Estante(models.Model):     
    categoria = models.CharField(max_length=50)

#Relacionamento 1:n - Um(a) escritor(a) pode escrever vários livros(estou considerando que um livro é escrito somente por uma pessoa)
class Livro(models.Model): 
    nome = models.CharField(max_length=50)
    edicao = models.CharField(max_length=30)
    ano = models.IntegerField()
    ibsn = models.CharField(max_length=13)
    escritor = models.ForeignKey(Escritor, on_delete=CASCADE, null=True)
    estante = models.ForeignKey(Estante, on_delete=CASCADE, null=True)

#Relacionamento n:n - Um usuário pode emprestar vários livros
class Usuario(models.Model): 
    nome = models.CharField(max_length=50)

#Relacionamento n:n e 1:n, um livro pode ser emprestado uma única vez, mas vários livros podem ser emprestados a vários usuários
class Emprestimo(models.Model): 
    livro = ForeignKey(Livro, on_delete=CASCADE, null=True)
    usuario = ForeignKey(Usuario, on_delete=CASCADE, null=True)
    data = models.DateTimeField(auto_now=True, blank=True)
