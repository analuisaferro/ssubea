from django.db import models
from autenticacao.models import *
# Create your models here.



class Tipo(models.Model):

    def __str__(self):
        return '%s' % (self.nome)

    class Meta:
        ordering = ['nome']
    nome=models.CharField(max_length=64, verbose_name='', blank=False, null=False)

class Animal(models.Model):

    SEXO_CHOICES=[
        ('m', 'Macho'), 
        ('f', 'Fêmea'),
    ]
    nome=models.CharField(max_length=64, verbose_name='Nome/apelido', blank=True, null=True)
    tipo=models.ForeignKey(Tipo, on_delete=models.PROTECT, blank=False, null=False)
    tutor=models.ForeignKey(Tutor, on_delete=models.PROTECT, blank=False, null=False)
    sexo=models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo do animal', blank=False, null=False)
    castrado=models.BooleanField(default=False, verbose_name='Castrado')
    dt_inclusao=models.DateField(auto_now_add=True, verbose_name='Data de inclusão')

class Ave(models.Model):
    animal=models.ForeignKey(Animal, on_delete=models.CASCADE, blank=True, null=True) 
    anilha=models.CharField(max_length=64, verbose_name='Código da anilha', blank=True, null=True)
    especie=models.CharField(max_length=64, verbose_name='Espécie', blank=True, null=True)