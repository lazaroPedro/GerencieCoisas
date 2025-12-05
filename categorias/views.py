from django.shortcuts import render, redirect, get_object_or_404
from categorias.forms import CategoriaForm
from categorias.models import Categoria
from django.contrib.auth.decorators import login_required, permission_required
from movimentacoes.utils import registrar_movimentacao
from movimentacoes.models import Movimentacao

@login_required
@permission_required("categorias.view_categoria", raise_exception=True)
def index(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias/index.html", {"categorias": categorias})

@login_required
@permission_required("categorias.add_categoria", raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()

            registrar_movimentacao(
                usuario=request.user,
                acao=Movimentacao.ACAO_CRIACAO,
                instance=categoria,
                descricao=f"Categoria criada: {categoria} (ID {categoria.pk})",
            )

            return redirect('categorias:index')
    else:

        form = CategoriaForm()

    return render(request, 'categorias/create.html', {'form': form})
@login_required
@permission_required("categorias.change_categoria", raise_exception=True)
def edit(request, pk):
    categorias = Categoria.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categorias)
        if form.is_valid():
            categoria = form.save()

            registrar_movimentacao(
                usuario=request.user,
                acao=Movimentacao.ACAO_EDICAO,
                instance=categoria,
                descricao=f"Categoria editada: {categoria} (ID {categoria.pk})",
            )
            return redirect('categorias:index')
    else:
        form = CategoriaForm(instance=categorias)
    return render(request, 'categorias/edit.html', {'form': form, "categorias": categorias})
@login_required
@permission_required("categorias.delete_categoria", raise_exception=True)
def delete(request, pk):
    categorias = Categoria.objects.get(id=pk)
    if request.method == 'POST':
        categoria_repr = str(categorias)

        registrar_movimentacao(
            usuario=request.user,
            acao=Movimentacao.ACAO_EXCLUSAO,
            instance=categorias,
            descricao=f"Categoria excluída: {categoria_repr}",
        )

        categorias.delete()
        return redirect('categorias:index')
    else:
        form = CategoriaForm(instance=categorias)
    return render(request, 'categorias/delete.html', {'form': form, "categorias": categorias})
@login_required
@permission_required("categorias.view_categoria", raise_exception=True)
def detail(request, pk):
    categorias = Categoria.objects.get(id=pk)
    return render(request, 'categorias/detail.html', {'categorias': categorias})
