from django.shortcuts import render, redirect, get_object_or_404
from produtos.forms import ProdutoForm, ProdutoEditForm
from produtos.models import Produto
from django.contrib.auth.decorators import login_required, permission_required
from movimentacoes.utils import registrar_movimentacao
from movimentacoes.models import Movimentacao

                        
@login_required
@permission_required("produtos.view_produto", raise_exception=True)
def index(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/index.html", {"produtos": produtos})

@login_required
@permission_required("produtos.add_produto", raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()

            registrar_movimentacao(
                usuario=request.user,
                acao=Movimentacao.ACAO_CRIACAO,
                instance=produto,
                descricao=f"Produto criado: {produto.name} (ID {produto.pk})",
            )
            return redirect("produtos:index")

    else:

        form = ProdutoForm()

    return render(request, 'produtos/create.html', {'form': form})

@login_required
@permission_required("produtos.change_produto", raise_exception=True)
def edit(request, pk):
    produto = Produto.objects.get(id=pk)
    if request.method == 'POST':
        form = ProdutoEditForm(request.POST, instance=produto)
        if form.is_valid():
            produto = form.save()

            registrar_movimentacao(
                usuario=request.user,
                acao=Movimentacao.ACAO_EDICAO,
                instance=produto,
                descricao=f"Produto editado: {produto.name} (ID {produto.pk})",
            )

            return redirect("produtos:index")
    else:
        form = ProdutoEditForm(instance=produto)
    return render(request, 'produtos/edit.html', {'form': form, 'produto': produto})

@login_required
@permission_required("produtos.delete_produto", raise_exception=True)
def delete(request, pk):
    produto = Produto.objects.get(id=pk)

    if request.method == "POST":
        descricao = f"Produto excluído: {produto.name} (ID {produto.pk})"

        registrar_movimentacao(
            usuario=request.user,
            acao=Movimentacao.ACAO_EXCLUSAO,
            instance=produto,
            descricao=descricao,
        )

        produto.delete()
        
        return redirect('produtos:index')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/delete.html', {'form': form, 'produto': produto})

@login_required
@permission_required("produtos.view_produto", raise_exception=True)
def detail(request, pk):
    produto = Produto.objects.get(id=pk)
    return render(request, 'produtos/detail.html', {'produto': produto})