from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required   
from categorias.models import Categoria
from fornecedores.models import Fornecedor
from produtos.models import Produto

from django.db.models import Sum, F

@login_required
def index(request):
    # Contadores Simples
    total_produtos = Produto.objects.count()
    total_categorias = Categoria.objects.count()
    total_fornecedores = Fornecedor.objects.count()

    # Calcular Valor Total do Stock (Preço * Quantidade de cada item)
    valor_estoque = Produto.objects.aggregate(
        total=Sum(F('price') * F('quantity'))
    )['total'] or 0

    # Alerta: Produtos ativos com menos de 5 unidades
    produtos_baixo_estoque = Produto.objects.filter(quantity__lt=5, active=True)

    # Últimos produtos cadastrados para a tabela rápida
    ultimos_produtos = Produto.objects.all().order_by('-id')[:5]

    context = {
        'total_produtos': total_produtos,
        'total_categorias': total_categorias,
        'total_fornecedores': total_fornecedores,
        'valor_estoque': valor_estoque,
        'baixo_estoque_count': produtos_baixo_estoque.count(),
        'ultimos_produtos': ultimos_produtos
    }

    return render(request, 'dashboard/index.html', context)
