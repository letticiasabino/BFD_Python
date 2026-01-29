from django.db import models

# Create your models here.

from django.db import models

class Pessoa(models.Model):
  nome = models.CharField(max_length=100)
  email = models.EmailField()
  idade = models.IntegerField()
  telefone = models.CharField(max_length=20)
  cidade = models.CharField(max_length=100)
  profissao = models.CharField(max_length=100)
  mensagem = models.TextField()

  def __str__(self):
    return self.nome