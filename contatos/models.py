from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.nome

