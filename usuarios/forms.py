# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        labels = {
            "first_name": "Nome",
            "last_name": "Sobrenome",
            "email": "E-mail",
        }

class GerenteEditForm(forms.ModelForm):
    """
    Form para editar dados do gerente + permissões (produtos/categorias/fornecedores).
    Não mexe em senha aqui.
    """

    manage_produtos = forms.BooleanField(
        required=False,
        label="Gerenciar Produtos (CRUD)",
    )
    manage_categorias = forms.BooleanField(
        required=False,
        label="Gerenciar Categorias (CRUD)",
    )
    manage_fornecedores = forms.BooleanField(
        required=False,
        label="Gerenciar Fornecedores (CRUD)",
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        labels = {
            "username": "Usuário (login)",
            "first_name": "Nome",
            "last_name": "Sobrenome",
            "email": "E-mail",
        }


class GerenteCreationForm(UserCreationForm):
    """
    Formulário para o DONO criar um novo usuário gerente
    e definir quais áreas ele pode administrar.
    """

    first_name = forms.CharField(label="Nome", max_length=150)
    last_name = forms.CharField(label="Sobrenome", max_length=150, required=False)
    email = forms.EmailField(label="E-mail")

    manage_produtos = forms.BooleanField(
        required=False,
        label="Gerenciar Produtos (CRUD)",
    )
    manage_categorias = forms.BooleanField(
        required=False,
        label="Gerenciar Categorias (CRUD)",
    )
    manage_fornecedores = forms.BooleanField(
        required=False,
        label="Gerenciar Fornecedores (CRUD)",
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
