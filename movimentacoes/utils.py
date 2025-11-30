# movimentacoes/utils.py
from django.contrib.contenttypes.models import ContentType
from .models import Movimentacao


def registrar_movimentacao(*, usuario, acao, instance, descricao=""):
    """
    Registra uma movimentação genérica (create/update/delete) para qualquer model.

    Parâmetros:
    - usuario: request.user (pode ser anônimo, será salvo como None)
    - acao: uma das constantes de Movimentacao (ACAO_CRIACAO, ACAO_EDICAO, ACAO_EXCLUSAO)
    - instance: instância do model afetado (Produto, Categoria, Fornecedor, etc.)
    - descricao: texto livre opcional
    """
    content_type = ContentType.objects.get_for_model(instance.__class__)

    Movimentacao.objects.create(
        usuario=usuario if usuario.is_authenticated else None,
        content_type=content_type,
        object_id=instance.pk,
        acao=acao,
        descricao=descricao,
    )
