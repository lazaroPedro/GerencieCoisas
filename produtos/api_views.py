from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from GerencieCoisas.api_permissions import DjangoModelPermissionsWithView
from GerencieCoisas.pagination import StandardResultsSetPagination
from produtos.models import Produto
from produtos.serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = (
        Produto.objects.select_related("category")
        .prefetch_related("supplier")
        .all()
        .order_by("id")
    )
    serializer_class = ProdutoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissionsWithView]
    pagination_class = StandardResultsSetPagination
