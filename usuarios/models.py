from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
    nome = models.CharField("Nome da empresa", max_length=255)
    cnpj = models.CharField("CNPJ", max_length=18, blank=True, null=True, unique=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    ativo = models.BooleanField("Ativa?", default=True)

    def __str__(self):
        return self.nome


class PerfilUsuario(models.Model):
    TIPO_MASTER = 'MASTER'
    TIPO_GERENTE = 'GERENTE'
    TIPO_ASSISTENTE = 'ASSISTENTE'

    TIPOS_CHOICES = [
        (TIPO_MASTER, 'Gerente geral (dono)'),
        (TIPO_GERENTE, 'Gerente local'),
        (TIPO_ASSISTENTE, 'Assistente'),
    ]

    ESCOPO_PRODUTOS = 'PRODUTOS'
    ESCOPO_CATEGORIAS = 'CATEGORIAS'
    ESCOPO_FORNECEDORES = 'FORNECEDORES'
    ESCOPO_MOVIMENTACOES = 'MOVIMENTACOES'

    ESCOPO_CHOICES = [
        (ESCOPO_PRODUTOS, 'Produtos'),
        (ESCOPO_CATEGORIAS, 'Categorias'),
        (ESCOPO_FORNECEDORES, 'Fornecedores'),
        (ESCOPO_MOVIMENTACOES, 'Movimentações de estoque'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil',
        verbose_name='Usuário de login',
    )

    tipo = models.CharField(
        "Tipo de usuário",
        max_length=20,
        choices=TIPOS_CHOICES,
    )

    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='perfis',
        verbose_name="Empresa",
    )

    gerente_geral = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='gerentes_subordinados',
        verbose_name="Gerente geral (dono)",
        limit_choices_to={'tipo': TIPO_MASTER},
    )

    gerente = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='assistentes',
        verbose_name="Gerente direto",
        limit_choices_to={'tipo': TIPO_GERENTE},
    )

    escopo = models.CharField(
        "Escopo de gestão",
        max_length=20,
        choices=ESCOPO_CHOICES,
        null=True,
        blank=True,
        help_text="Somente para gerente local: define a área que ele administra.",
    )

    criado_em = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return f'{self.user.get_full_name() or self.user.username} ({self.get_tipo_display()})'

    @property
    def is_master(self):
        return self.tipo == self.TIPO_MASTER

    @property
    def is_gerente(self):
        return self.tipo == self.TIPO_GERENTE

    @property
    def is_assistente(self):
        return self.tipo == self.TIPO_ASSISTENTE