from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from fornecedores.forms import FornecedorForm
from fornecedores.models import Fornecedor
from movimentacoes.utils import registrar_movimentacao
from movimentacoes.models import Movimentacao

@login_required
@permission_required("fornecedores.view_fornecedor", raise_exception=True)
def index(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "fornecedores/index.html", {"fornecedores": fornecedores})

@login_required
@permission_required("fornecedores.add_fornecedor", raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            fornecedor = form.save()

            registrar_movimentacao(
                usuario=request.user,
                acao=Movimentacao.ACAO_CRIACAO,
                instance=fornecedor,
                descricao=f"Fornecedor criado: {fornecedor} (ID {fornecedor.pk})",
            )


            return redirect('fornecedores:index')
    else:
        form = FornecedorForm()

    return render(request, 'fornecedores/create.html', {'form': form})

@login_required
@permission_required("fornecedores.change_fornecedor", raise_exception=True)
def edit(request, pk):
    fornecedor = Fornecedor.objects.get(id=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            fornecedor = form.save()

            # registra movimentação de edição
            registrar_movimentacao(
                usuario=request.user,
                acao=Movimentacao.ACAO_EDICAO,
                instance=fornecedor,
                descricao=f"Fornecedor editado: {fornecedor} (ID {fornecedor.pk})",
            )

            return redirect('fornecedores:index')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedores/edit.html', {'form': form, 'fornecedor': fornecedor})

@login_required
@permission_required("fornecedores.delete_fornecedor", raise_exception=True)
def delete(request, pk):
    fornecedor = Fornecedor.objects.get(id=pk)
    if request.method == 'POST':
        fornecedor_repr = str(fornecedor)

        # registra movimentação de exclusão
        registrar_movimentacao(
            usuario=request.user,
            acao=Movimentacao.ACAO_EXCLUSAO,
            instance=fornecedor,
            descricao=f"Fornecedor excluído: {fornecedor_repr}",
        )

        fornecedor.delete()

        return redirect('fornecedores:index')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedores/delete.html', {'form': form, 'fornecedor': fornecedor})

@login_required
@permission_required("fornecedores.view_fornecedor", raise_exception=True)
def detail(request, pk):
    fornecedor = Fornecedor.objects.get(id=pk)
    return render(request, 'fornecedores/detail.html', {'fornecedor': fornecedor})