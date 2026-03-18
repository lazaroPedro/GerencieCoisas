from django.urls import path, include
from rest_framework.routers import DefaultRouter
from categorias.api_views import CategoriaViewSet
from fornecedores.api_views import FornecedorViewSet
from produtos.api_views import ProdutoViewSet
from movimentacoes.api_views import MovimentacaoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'fornecedores', FornecedorViewSet, basename='fornecedor')
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'movimentacoes', MovimentacaoViewSet, basename='movimentacao')

urlpatterns = [
    path('', include(router.urls)),
]
