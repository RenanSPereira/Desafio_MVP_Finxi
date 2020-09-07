from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Demanda(models.Model):
    STATUS = (
        ('aberta', 'Aberta'),
        ('fechada', 'Fechada')
    )
    descricao_peca = models.CharField(max_length=70)
    informacao_contato = models.CharField(max_length=100)
    anunciante = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status_finalizacao = models.CharField(max_length=10, choices=STATUS, default='aberta')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    logradouro = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    uf = models.CharField(max_length=2, null=False, blank=False)
    cep = models.IntegerField()

    def __str__(self):
        return self.descricao_peca
