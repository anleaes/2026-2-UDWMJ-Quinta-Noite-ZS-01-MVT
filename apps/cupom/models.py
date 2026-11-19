from django.db import models
from evento.models import Evento

# Create your models here.

class Cupom(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    codigo = models.CharField('Código', max_length=50)
    percentual_desconto = models.FloatField('Percentual de desconto', null=True, blank=True, default=0.0)
    validade = models.DateField('Validade', auto_now=False, auto_now_add=False)
    ativo = models.BooleanField('Ativo', default=False)

    class Meta:
        verbose_name = 'Cupom'
        verbose_name_plural = 'Cupons'
        ordering = ['id']

    def __str__(self):
        return f'{self.codigo}'
