from rest_framework import viewsets
from movimentacoes.models import Movimentacao
from GerencieCoisas.serializers import MovimentacaoSerializer

class MovimentacaoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows movements to be viewed.
    """
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer
