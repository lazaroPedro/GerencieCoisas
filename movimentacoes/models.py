from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Movimentacao(models.Model):
    ACAO_CRIACAO = "create"
    ACAO_EDICAO = "update"
    ACAO_EXCLUSAO = "delete"

    ACAO_CHOICES = (
        (ACAO_CRIACAO, "Criação"),
        (ACAO_EDICAO, "Edição"),
        (ACAO_EXCLUSAO, "Exclusão"),
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="movimentacoes",
        verbose_name="Usuário",
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name="Tipo de objeto",
    )
    object_id = models.PositiveIntegerField("ID do objeto")
    content_object = GenericForeignKey("content_type", "object_id")

    acao = models.CharField(
        "Ação",
        max_length=10,
        choices=ACAO_CHOICES,
    )

    descricao = models.TextField(
        "Descrição",
        blank=True,
    )

    criado_em = models.DateTimeField(
        "Data/Hora",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"
        ordering = ["-criado_em"]

    def __str__(self):
        usuario = self.usuario.get_username() if self.usuario else "Sistema"
        return f"{self.get_acao_display()} por {usuario} em {self.criado_em:%d/%m/%Y %H:%M}"
