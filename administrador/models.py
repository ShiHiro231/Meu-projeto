from django.db import models


class Administrador(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome_evento = models