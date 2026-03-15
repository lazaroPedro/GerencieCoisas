"""
URL configuration for GerencieCoisas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dashboard.views import index
from categorias.api_views import CategoriaViewSet
from fornecedores.api_views import FornecedorViewSet
from produtos.api_views import ProdutoViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet, basename="api-categorias")
router.register(r"fornecedores", FornecedorViewSet, basename="api-fornecedores")
router.register(r"produtos", ProdutoViewSet, basename="api-produtos")

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('categorias/', include('categorias.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('conta/', include('usuarios.urls')),
    path("movimentacoes/", include("movimentacoes.urls")),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
