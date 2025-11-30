from django.contrib import admin
from .models import Empresa, PerfilUsuario


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'ativo', 'criado_em')
    search_fields = ('nome', 'cnpj')
    list_filter = ('ativo',)


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'tipo', 'empresa', 'gerente_geral', 'gerente', 'criado_em')
    list_filter = ('tipo', 'empresa')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')
