from django.db import models

# Create your models here.

class Atracao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=300)
    cache = models.DecimalField('Cachê', max_digits=10, decimal_places=2, default=0)
    foto = models.ImageField('Foto', upload_to='photos')

    class Meta:
        verbose_name = 'Atração'
        verbose_name_plural = 'Atrações'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome}'
