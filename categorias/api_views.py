from rest_framework import viewsets
from categorias.models import Categoria
from GerencieCoisas.serializers import CategoriaSerializer

class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows categories to be viewed.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
