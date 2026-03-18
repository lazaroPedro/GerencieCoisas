from rest_framework import viewsets
from fornecedores.models import Fornecedor
from GerencieCoisas.serializers import FornecedorSerializer

class FornecedorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows suppliers to be viewed.
    """
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
