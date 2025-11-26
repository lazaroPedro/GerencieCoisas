from django.shortcuts import render, redirect

from produtos.forms import ProdutoForm, ProdutoEditForm
from produtos.models import Produto


# Create your views here.

def index(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/index.html", {"produtos": produtos})

def create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:

        form = ProdutoForm()

    return render(request, 'produtos/create.html', {'form': form})

def edit(request, pk):
    produto = Produto.objects.get(id=pk)
    if request.method == 'POST':
        form = ProdutoEditForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdutoEditForm(instance=produto)
    return render(request, 'produtos/edit.html', {'form': form, 'produto': produto})

def delete(request, pk):
    produto = Produto.objects.get(id=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('index')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/delete.html', {'form': form, 'produto': produto})



