from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from GerencieCoisas.api_permissions import DjangoModelPermissionsWithView
from GerencieCoisas.pagination import StandardResultsSetPagination
from fornecedores.models import Fornecedor
from fornecedores.serializers import FornecedorSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all().order_by("id")
    serializer_class = FornecedorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissionsWithView]
    pagination_class = StandardResultsSetPagination
