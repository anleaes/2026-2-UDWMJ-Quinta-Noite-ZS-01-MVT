from django.db import models
from pedido.models import Pedido
from lote.models import Lote

# Create your models here.

class Ingresso(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    codigo = models.CharField('Código', max_length=50)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    meia_entrada = models.BooleanField('Meia entrada', default=False)

    class Meta:
        verbose_name = 'Ingresso'
        verbose_name_plural = 'Ingressos'
        ordering = ['id']

    def __str__(self):
        return f'{self.codigo}'
