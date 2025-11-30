from django.contrib import admin
from .models import Movimentacao


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ("criado_em", "usuario", "acao", "content_type", "object_id")
    list_filter = ("acao", "content_type", "usuario")
    search_fields = ("descricao", "usuario__username")
    date_hierarchy = "criado_em"
