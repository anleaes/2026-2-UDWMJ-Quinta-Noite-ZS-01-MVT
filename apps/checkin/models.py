from django.db import models
from ingresso.models import Ingresso

# Create your models here.

class CheckIn(models.Model):
    ingresso = models.OneToOneField(Ingresso, on_delete=models.CASCADE)
    data_hora = models.DateTimeField('Data e hora', auto_now=False, auto_now_add=False)
    portao = models.CharField('Portão', max_length=50)
    observacao = models.TextField('Observação', max_length=300, blank=True)

    class Meta:
        verbose_name = 'Check-in'
        verbose_name_plural = 'Check-ins'
        ordering = ['id']

    def __str__(self):
        return f'Check-in do {self.ingresso}'
