from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Pessoa(models.Model):

    def __str__(self):
        return '%s' % (self.email)
    
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome=models.CharField(max_length=64, verbose_name='Nome', blank=False, null=False)
    email=models.EmailField()
    cpf=models.CharField(max_length=14, verbose_name='CPF', blank=False, null=False, unique=True)
    telefone=models.CharField(max_length=15, verbose_name='Telefone', blank=True, null=True)
    dt_nascimento=models.DateField(verbose_name='Data de nascimento', blank=False, null=False)
    bairro=models.CharField(max_length=64, verbose_name='Bairro', blank=False, null=False)
    endereco=models.CharField(max_length=128, verbose_name='Endereco', blank=False, null=False)
    complemento=models.CharField(max_length=128, verbose_name='Complemento', blank=False, null=False)
    dt_inclusao=models.DateField(auto_now_add=True, verbose_name='Data de inclusão')
