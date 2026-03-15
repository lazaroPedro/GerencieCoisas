from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from GerencieCoisas.api_permissions import DjangoModelPermissionsWithView
from GerencieCoisas.pagination import StandardResultsSetPagination
from categorias.models import Categoria
from categorias.serializers import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.select_related("parent").all().order_by("id")
    serializer_class = CategoriaSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissionsWithView]
    pagination_class = StandardResultsSetPagination
