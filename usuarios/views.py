from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render, get_object_or_404

from .forms import GerenteCreationForm, PerfilForm, GerenteEditForm
from movimentacoes.utils import registrar_movimentacao
from movimentacoes.models import Movimentacao


@login_required
def perfil_view(request):
    user = request.user

    if request.method == "POST":
        dados_anteriores = model_to_dict(user)

        form = PerfilForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()

            dados_novos = model_to_dict(user)

            descricao = (
                f"Perfil do usuário '{user.username}' atualizado. "
                f"Dados anteriores: {dados_anteriores}. "
                f"Dados novos: {dados_novos}."
            )

            registrar_movimentacao(
                usuario=request.user,
                acao=Movimentacao.ACAO_EDICAO,
                instance=user,
                descricao=descricao,
            )

            messages.success(request, "Perfil atualizado com sucesso.")
            return redirect("perfil")
    else:
        form = PerfilForm(instance=user)

    return render(request, "usuarios/perfil.html", {"form": form})


@login_required
@permission_required("auth.add_user", raise_exception=True)
def listar_gerentes(request):
    grupos_gerente = Group.objects.filter(
        name__in=["GerenteProdutos", "GerenteCategorias", "GerenteFornecedores"]
    )
    gerentes = User.objects.filter(groups__in=grupos_gerente).distinct()

    return render(request, "usuarios/listar_gerentes.html", {"gerentes": gerentes})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login realizado com sucesso.")
            return redirect("index")
    else:
        form = AuthenticationForm(request)

    return render(request, "usuarios/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso.")
    return redirect("login")


def _ensure_group_with_perms(group_name: str, app_label: str, model_name: str) -> Group:
    group, _created = Group.objects.get_or_create(name=group_name)

    perms_codenames = [
        f"add_{model_name}",
        f"change_{model_name}",
        f"delete_{model_name}",
        f"view_{model_name}",
    ]

    perms = Permission.objects.filter(
        content_type__app_label=app_label,
        codename__in=perms_codenames,
    )

    group.permissions.set(perms)
    return group


@login_required
@permission_required("auth.add_user", raise_exception=True)
def criar_gerente(request):
    if request.method == "POST":
        form = GerenteCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get("first_name", "")
            user.last_name = form.cleaned_data.get("last_name", "")
            user.email = form.cleaned_data.get("email", "")
            user.is_staff = True
            user.save()

            data = form.cleaned_data

            if data.get("manage_produtos"):
                grp_prod = _ensure_group_with_perms(
                    "GerenteProdutos", "produtos", "produto"
                )
                user.groups.add(grp_prod)

            if data.get("manage_categorias"):
                grp_cat = _ensure_group_with_perms(
                    "GerenteCategorias", "categorias", "categoria"
                )
                user.groups.add(grp_cat)

            if data.get("manage_fornecedores"):
                grp_forn = _ensure_group_with_perms(
                    "GerenteFornecedores", "fornecedores", "fornecedor"
                )
                user.groups.add(grp_forn)

            permissoes = []
            if data.get("manage_produtos"):
                permissoes.append("produtos")
            if data.get("manage_categorias"):
                permissoes.append("categorias")
            if data.get("manage_fornecedores"):
                permissoes.append("fornecedores")

            descricao = (
                f"Gerente criado: {user.get_username()} "
                f"({user.get_full_name() or 'sem nome completo'}) "
                f"com acesso a: {', '.join(permissoes) if permissoes else 'nenhum módulo'}"
            )

            registrar_movimentacao(
                usuario=request.user,
                acao=Movimentacao.ACAO_CRIACAO,
                instance=user,
                descricao=descricao,
            )

            messages.success(request, "Gerente criado com sucesso.")
            return redirect("index")
    else:
        form = GerenteCreationForm()

    return render(request, "usuarios/criar_gerente.html", {"form": form})


@login_required
@permission_required("auth.add_user", raise_exception=True)
def editar_gerente(request, user_id):
    gerente = get_object_or_404(User, pk=user_id)

    is_gerente_prod = gerente.groups.filter(name="GerenteProdutos").exists()
    is_gerente_cat = gerente.groups.filter(name="GerenteCategorias").exists()
    is_gerente_forn = gerente.groups.filter(name="GerenteFornecedores").exists()

    if request.method == "POST":
        form = GerenteEditForm(request.POST, instance=gerente)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            data = form.cleaned_data

            grp_prod = _ensure_group_with_perms(
                "GerenteProdutos", "produtos", "produto"
            )
            grp_cat = _ensure_group_with_perms(
                "GerenteCategorias", "categorias", "categoria"
            )
            grp_forn = _ensure_group_with_perms(
                "GerenteFornecedores", "fornecedores", "fornecedor"
            )

            gerente.groups.remove(grp_prod, grp_cat, grp_forn)

            permissoes = []
            if data.get("manage_produtos"):
                gerente.groups.add(grp_prod)
                permissoes.append("produtos")
            if data.get("manage_categorias"):
                gerente.groups.add(grp_cat)
                permissoes.append("categorias")
            if data.get("manage_fornecedores"):
                gerente.groups.add(grp_forn)
                permissoes.append("fornecedores")

            descricao = (
                f"Gerente editado: {gerente.get_username()} "
                f"({gerente.get_full_name() or 'sem nome completo'}) "
                f"com acesso a: {', '.join(permissoes) if permissoes else 'nenhum módulo'}"
            )

            registrar_movimentacao(
                usuario=request.user,
                acao=Movimentacao.ACAO_EDICAO,
                instance=gerente,
                descricao=descricao,
            )

            messages.success(request, "Gerente atualizado com sucesso.")
            return redirect("listar_gerentes")
    else:
        form = GerenteEditForm(
            instance=gerente,
            initial={
                "manage_produtos": is_gerente_prod,
                "manage_categorias": is_gerente_cat,
                "manage_fornecedores": is_gerente_forn,
            },
        )

    return render(
        request,
        "usuarios/editar_gerente.html",
        {"form": form, "gerente": gerente},
    )


@login_required
def password_change_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            registrar_movimentacao(
                usuario=request.user,
                acao=Movimentacao.ACAO_EDICAO,
                instance=user,
                descricao=f"Senha do usuário '{user.username}' alterada.",
            )

            messages.success(request, "Sua senha foi alterada com sucesso.")
            return redirect("password_change_done")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "usuarios/password_change.html", {"form": form})


@login_required
def password_change_done_view(request):
    return render(request, "usuarios/password_change_done.html")