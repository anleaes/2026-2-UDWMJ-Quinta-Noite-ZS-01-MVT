from django.db import models

# Create your models here.

class Organizador(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)
    logo = models.ImageField('Logo', upload_to='photos')

    class Meta:
        verbose_name = 'Organizador'
        verbose_name_plural = 'Organizadores'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome}'
