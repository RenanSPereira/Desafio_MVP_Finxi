from django.contrib import admin
from .models import Demanda
from django.utils.html import format_html

# Register your models here.


@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    list_display = (
        'descricao_peca',
        'informacao_contato',
        'finalizado',
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

    def finalizado(self, obj):
        tag = "<img src='/static/img/{}' />"
        if not obj.status_finalizacao:
            return format_html(tag.format("baseline-highlight_off.svg"))
        else:
            return format_html(tag.format("baseline-check_circle_outline.svg"))
