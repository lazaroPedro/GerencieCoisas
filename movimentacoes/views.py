from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from produtos.models import Produto 

from .models import Movimentacao


@login_required
def lista_movimentacoes(request):
    user = request.user

    if user.has_perm("auth.add_user"):
        qs = Movimentacao.objects.all()

    else:
        app_labels_permitidos = []

        if user.groups.filter(name="GerenteProdutos").exists():
            app_labels_permitidos.append("produtos")

        if user.groups.filter(name="GerenteCategorias").exists():
            app_labels_permitidos.append("categorias")

        if user.groups.filter(name="GerenteFornecedores").exists():
            app_labels_permitidos.append("fornecedores")

        if app_labels_permitidos:
            qs = Movimentacao.objects.filter(
                content_type__app_label__in=app_labels_permitidos
            )
        else:
            qs = Movimentacao.objects.filter(usuario=user)

    qs = qs.select_related("usuario", "content_type").order_by("-criado_em")

    return render(
        request,
        "movimentacoes/lista_movimentacoes.html",
        {"movimentacoes": qs},
    )
