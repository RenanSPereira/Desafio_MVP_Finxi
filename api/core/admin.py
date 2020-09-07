from django.contrib import admin
from .models import Demanda


# Register your models here.


@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = (
        'descricao_peca',
        'informacao_contato',
        'status_finalizacao',
        'anunciante',
        'data_cadastro',
    )

    fields = (
        'descricao_peca',
        'informacao_contato',
        'status_finalizacao',
        'logradouro',
        'numero',
        'complemento',
        'bairro',
        'cidade',
        'uf',
        'cep',
    )

    def save_model(self, request, obj, form, change):
        obj.anunciante = request.user
        super(DemandaAdmin, self).save_model(request, obj, form, change)
