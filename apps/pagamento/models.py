from django.db import models
from pedido.models import Pedido

# Create your models here.

METODO_CHOICES = [
    ('pix', 'Pix'),
    ('credito', 'Cartão de crédito'),
    ('debito', 'Cartão de débito'),
    ('boleto', 'Boleto'),
]

class Pagamento(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    metodo = models.CharField('Método', max_length=20, choices=METODO_CHOICES)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    aprovado = models.BooleanField('Aprovado', default=False)
    comprovante = models.FileField('Comprovante', upload_to='docs', blank=True)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['id']

    def __str__(self):
        return f'Pagamento do {self.pedido}'
