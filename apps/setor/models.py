from django.db import models
from local.models import Local

# Create your models here.

class Setor(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    capacidade = models.IntegerField('Capacidade')
    coberto = models.BooleanField('Coberto', default=False)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} - {self.local}'
