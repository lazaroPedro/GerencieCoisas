# movimentacoes/urls.py
from django.urls import path
from . import views

app_name = "movimentacoes"

urlpatterns = [
    path("", views.lista_movimentacoes, name="lista"),
]
