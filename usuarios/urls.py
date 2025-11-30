# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("perfil/", views.perfil_view, name="perfil"),

    path("gerentes/", views.listar_gerentes, name="listar_gerentes"),
    path("gerentes/criar/", views.criar_gerente, name="criar_gerente"),
    path("gerentes/<int:user_id>/editar/", views.editar_gerente, name="editar_gerente"),

    path("senha/alterar/", views.password_change_view, name="password_change"),
    path("senha/alterar/concluido/", views.password_change_done_view, name="password_change_done"),
]
