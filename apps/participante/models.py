from django.db import models

# Create your models here.

class Participante(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=14)
    email = models.EmailField('E-mail', max_length=100)
    data_nascimento = models.DateField('Data de nascimento')
    foto = models.ImageField('Foto', upload_to='photos')

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome}'
