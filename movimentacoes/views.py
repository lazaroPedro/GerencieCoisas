from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from .models import Movimentacao
from produtos.models import Produto

def _is_master(user):
    if user.is_superuser:
        return True
    if hasattr(user, 'perfil') and user.perfil.tipo == 'MASTER':
        return True
    return False

@login_required
def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.select_related('usuario', 'content_type').all()
    
    is_master = _is_master(request.user)
    
    for mov in movimentacoes:
        mov.pode_alterar = is_master or (mov.usuario == request.user)

    return render(request, 'movimentacoes/lista_movimentacoes.html', {
        'movimentacoes': movimentacoes
    })

@login_required
def cadastro_movimentacao_produto(request):
    if request.method == "POST":
        try:
            produto_id = request.POST.get("produto")
            quantidade = int(request.POST.get("quantidade"))
            tipo_movimentacao = request.POST.get("tipo_movimentacao")
            
            produto = Produto.objects.get(id=produto_id)

            if tipo_movimentacao == "entrada":
                produto.quantity += quantidade
                acao_log = Movimentacao.ACAO_CRIACAO
                texto_tipo = "Entrada"
            elif tipo_movimentacao == "saida":
                if produto.quantity < quantidade:
                    messages.error(request, f"Estoque insuficiente. Atual: {produto.quantity}")
                    return redirect('movimentacoes:cadastro_movimentacao_produto')
                produto.quantity -= quantidade
                acao_log = Movimentacao.ACAO_EXCLUSAO 
                texto_tipo = "Saída"
            
            produto.save()

            Movimentacao.objects.create(
                usuario=request.user,
                content_type=ContentType.objects.get_for_model(produto),
                object_id=produto.id,
                acao=acao_log,
                descricao=f"Movimentação de Estoque: {texto_tipo} de {quantidade} unidades."
            )

            messages.success(request, "Movimentação registrada com sucesso!")
            return redirect('movimentacoes:lista_movimentacoes')

        except Exception as e:
            messages.error(request, f"Erro ao registrar: {str(e)}")

    produtos = Produto.objects.filter(active=True)
    return render(request, 'movimentacoes/cadastro_movimentacao_produto.html', {'produtos': produtos})

@login_required
def editar_movimentacao(request, pk):
    mov = get_object_or_404(Movimentacao, pk=pk)
    
    if not _is_master(request.user) and mov.usuario != request.user:
        messages.error(request, "Você não tem permissão para editar este registro.")
        return redirect('movimentacoes:lista_movimentacoes')

    if request.method == "POST":
        nova_descricao = request.POST.get("descricao")
        mov.descricao = nova_descricao
        mov.save()
        messages.success(request, "Registro atualizado.")
        return redirect('movimentacoes:lista_movimentacoes')
    
    return render(request, 'movimentacoes/editar_movimentacao.html', {'mov': mov})

@login_required
def deletar_movimentacao(request, pk):
    mov = get_object_or_404(Movimentacao, pk=pk)

    if not _is_master(request.user) and mov.usuario != request.user:
        messages.error(request, "Você não tem permissão para excluir este registro.")
        return redirect('movimentacoes:lista_movimentacoes')

    if request.method == "POST":
        mov.delete()
        messages.success(request, "Registro de movimentação excluído.")
        return redirect('movimentacoes:lista_movimentacoes')
    
    return redirect('movimentacoes:lista_movimentacoes')