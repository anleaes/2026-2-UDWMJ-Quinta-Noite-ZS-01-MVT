from django.db import models
from organizador.models import Organizador
from local.models import Local
from atracao.models import Atracao

# Create your models here.

class Evento(models.Model):
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    atracoes = models.ManyToManyField(Atracao, verbose_name='Atrações')
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    data_inicio = models.DateTimeField('Data de início', auto_now=False, auto_now_add=False)
    banner = models.ImageField('Banner', upload_to='photos')
    publicado = models.BooleanField('Publicado', default=False)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['id']

    def __str__(self):
        return f'{self.titulo}'
