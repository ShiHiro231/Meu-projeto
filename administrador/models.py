from django.db import models


class Administrador(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    nome_evento = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateField()
    horario_inicio = models.TimeField(blank=True, null=True)
    horario_fim = models.TimeField(blank=True, null=True)
    aceita_doacao = models.BooleanField(default=False)
    aceita_voluntariado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_evento} - {self.data}"

    class Meta:
        ordering = ['data', 'horario_inicio']