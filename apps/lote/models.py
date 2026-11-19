from django.db import models
from evento.models import Evento
from setor.models import Setor

# Create your models here.

class Lote(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2, default=0)
    quantidade = models.IntegerField('Quantidade', default=0)
    vendidos = models.IntegerField('Vendidos', default=0)
    ativo = models.BooleanField('Ativo', default=False)

    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'
        ordering = ['id']

    def __str__(self):
        return f'{self.evento} - {self.setor}'
