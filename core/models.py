from django.db import models
from autenticacao.models import *
# Create your models here.



class Tipo(models.Model):

    def __str__(self):
        return '%s' % (self.nome)

    class Meta:
        ordering = ['nome']
    nome=models.CharField(max_length=64, verbose_name='', blank=False, null=False)

class Periodo(models.Model):
    def __str__(self):
        return '%s' % (self.intervalo)
    
    intervalo = models.CharField(max_length=32, blank=False, null=False)
    
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
    animal_image = models.ImageField(upload_to='animal_tutor/', verbose_name="Foto do animal (opcional)",blank=True, null=True)
    dt_inclusao=models.DateField(auto_now_add=True, verbose_name='Data de inclusão')

class Informacoes_Extras(models.Model):
    class Meta:
        ordering = ['animal']

    animal=models.ForeignKey(Animal, on_delete=models.PROTECT)
    alimentacao_tipo=models.CharField(max_length=128, verbose_name='Tipo de alimentação', blank=True, null=True)
    alimentacao_periodo=models.ManyToManyField(Periodo, verbose_name='Período da alimentação')
    condicoes=models.CharField(max_length=128, verbose_name='Condições de abrigo na residência')
    dt_vacinacao=models.DateField(verbose_name='Data da última vacinação', auto_now=False, blank=True, null=True)
    dt_vermifugacao=models.DateField(verbose_name='Data da última vermifugação', auto_now=False, blank=True, null=True)
    complemento=models.CharField(max_length=256, verbose_name='Complemento', blank=True, null=True)
    dt_registro=models.DateField(verbose_name='Data do registro', blank=True, null=True)

class Errante(models.Model):

    # SEXO_CHOICES=[
    #     ('m', 'Macho'), 
    #     ('f', 'Fêmea'),
    #     ('n', 'Não identificado')
    # ]

    def __str__(self):
        return '%s' % (self.pelagem)
    
    
    pelagem=models.CharField(max_length=64, verbose_name="Pelagem", blank=False, null=False)
    tipo=models.ForeignKey(Tipo, on_delete=models.PROTECT, blank=False, null=False)
    especie=models.ForeignKey(Especie, on_delete=models.PROTECT, blank=True, null=True)
    animal_image = models.ImageField(upload_to='animal_errante/', verbose_name="Foto do animal (opcional)",blank=True, null=True)
    dt_inclusao=models.DateField(auto_now_add=True, verbose_name='Data de inclusão')

class Catalogo(models.Model):
    SEXO_CHOICES=[
        ('m', 'Macho'), 
        ('f', 'Fêmea'),
    ]

    pelagem=models.CharField(max_length=64, verbose_name="Pelagem", blank=False, null=False)
    idade=models.IntegerField(verbose_name='Idade', blank=True, null=True)
    raca=models.CharField(max_length=64, verbose_name='Raça', blank=True, null=True)
    sexo=models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo do animal', blank=False, null=False)
    castrado=models.BooleanField(default=False, verbose_name='Castrado')
    vacinado=models.BooleanField(default=False, verbose_name='Vacinado')
    animal_image = models.ImageField(upload_to='animal_catalogo/', verbose_name="Foto do animal (opcional)", blank=True, null=True)

