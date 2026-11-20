from django.db import models
from participante.models import Participante
from cupom.models import Cupom

# Create your models here.

STATUS_CHOICES = [
    ('pendente', 'Pendente'),
    ('pago', 'Pago'),
    ('cancelado', 'Cancelado'),
]

class Pedido(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    cupom = models.ForeignKey(Cupom, on_delete=models.SET_NULL, null=True, blank=True)
    data_pedido = models.DateTimeField('Data do pedido', auto_now=False, auto_now_add=False)
    valor_total = models.DecimalField('Valor total', max_digits=10, decimal_places=2, default=0)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

    def __str__(self):
        return f'Pedido {self.id} - {self.participante}'
