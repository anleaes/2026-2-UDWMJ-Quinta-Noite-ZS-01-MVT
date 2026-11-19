from django.db import models

# Create your models here.

class Local(models.Model):
    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('Endereço', max_length=200)
    capacidade_total = models.IntegerField('Capacidade total')
    mapa = models.ImageField('Mapa', upload_to='photos')

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome}'
