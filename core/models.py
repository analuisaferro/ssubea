from django.db import models
from autenticacao.models import *
# Create your models here.



class Tipo(models.Model):

    def __str__(self):
        return '%s' % (self.nome)

    class Meta:
        ordering = ['nome']
    nome=models.CharField(max_length=64, verbose_name='', blank=False, null=False)

class Especie(models.Model):

    def __str__(self):
        return '%s' % (self.nome_especie)
    
    class Meta:
         ordering= ['nome_especie']

    nome_especie=models.CharField(max_length=64, verbose_name='Espécie', blank=True, null=True)

class Animal(models.Model):

    SEXO_CHOICES=[
        ('m', 'Macho'), 
        ('f', 'Fêmea'),
    ]
    def __str__(self):
        return '%s' % (self.nome)
   
    nome=models.CharField(max_length=64, verbose_name='Nome/apelido', blank=True, null=True)
    tipo=models.ForeignKey(Tipo, on_delete=models.PROTECT, blank=False, null=False)
    especie=models.ForeignKey(Especie, on_delete=models.PROTECT, blank=True, null=True)
    tutor=models.ForeignKey(Tutor, on_delete=models.PROTECT, blank=False, null=False)
    sexo=models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo do animal', blank=False, null=False)
    castrado=models.BooleanField(default=False, verbose_name='Castrado')
    anilha=models.CharField(max_length=64, verbose_name='Código da anilha', blank=True, null=True)
    dt_inclusao=models.DateField(auto_now_add=True, verbose_name='Data de inclusão')


