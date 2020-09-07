from .models import Demanda
from django.contrib.auth.models import User
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class DemandaSerializer(serializers.ModelSerializer):
    # Usado para pegar nome do usuário vinculado a demanda
    anunciante = UsuarioSerializer()

    class Meta:
        model = Demanda
        fields = [
            'id',
            'descricao_peca',
            'informacao_contato',
            'status_finalizacao',
            'anunciante',
            'logradouro',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'uf',
            'cep',
        ]
