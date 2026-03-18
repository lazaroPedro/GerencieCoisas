from rest_framework import viewsets
from produtos.models import Produto
from GerencieCoisas.serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows products to be viewed.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
