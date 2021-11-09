from django.db import models

# Create your models here.
class Livro(models.Model):
    nome = models.CharField(max_length=50)
    edicao = models.CharField(max_length=30)
    ano = models.IntegerField(max_length=4)
    ibsn = models.CharField(max_length=13)