from django.urls import path
from . import views
from django.views.generic import RedirectView


app_name = "movimentacoes"

urlpatterns = [
    path('', RedirectView.as_view(url='/movimentacoes/cadastro/', permanent=False), name='home'), 
    path("lista/", views.lista_movimentacoes, name="lista_movimentacoes"),
    path("cadastro/", views.cadastro_movimentacao_produto, name="cadastro_movimentacao_produto"),
    path("<int:pk>/editar/", views.editar_movimentacao, name="editar_movimentacao"),
    path("<int:pk>/deletar/", views.deletar_movimentacao, name="deletar_movimentacao"),
]

