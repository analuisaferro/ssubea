from django.db import models

# Create your models here.

class Local(models.Model):
    bairro=models.CharField(max_length=64, verbose_name='Bairro', blank=False, null=False)
    endereco=models.CharField(max_length=128, verbose_name='Endereco', blank=False, null=False)
    complemento=models.CharField(max_length=128, verbose_name='Complemento', blank=False, null=False)

class Tutor(models.Model):

    TIPO_DE_MORADIA_CHOICES=[
        ('Própria', 'Própria'), 
        ('Alugada', 'Alugada'),
    ]
    nome=models.CharField(max_length=64, verbose_name='Nome', blank=False, null=False)
    cpf=models.CharField(max_length=14, verbose_name='CPF do tutor', blank=False, null=False)
    rg=models.CharField(max_length=10, verbose_name='Identidade', blank=False, null=False)
    dt_nascimento=models.DateField(verbose_name='Data de nascimento', blank=False, null=False)
    tipo_de_moradia=models.CharField(max_length=7, choices=TIPO_DE_MORADIA_CHOICES, verbose_name='Tipo de moradia', blank=False, null=False)
    dt_inclusao=models.DateField(auto_now_add=True, verbose_name='Data de inclusão')

class Tipo(models.Model):
    nome=models.CharField(max_length=64, verbose_name='', blank=False, null=False)

class Animal(models.Model):

    SEXO_CHOICES=[
        ('m', 'Macho'), 
        ('f', 'Fêmea'),
    ]
    tipo=models.ForeignKey(Tipo, on_delete=models.PROTECT, blank=False, null=False)
    tutor=models.ForeignKey(Tutor, on_delete=models.PROTECT, blank=False, null=False)
    sexo=models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo do animal', blank=False, null=False)
    castrado=models.BooleanField(default=False, verbose_name='Castrado')
    dt_inclusao=models.DateField(auto_now_add=True, verbose_name='Data de inclusão')

class Ave(models.Model):
    animal=models.ForeignKey(Animal, on_delete=models.PROTECT, blank=False, null=False)
    anilha=models.CharField(max_length=64, verbose_name='Código da anilha', blank=False, null=False)
    especie=models.CharField(max_length=64, verbose_name='Espécie', blank=False, null=False)