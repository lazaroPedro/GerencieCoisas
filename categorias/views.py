from django.shortcuts import render, redirect

from categorias.forms import CategoriaForm
from categorias.models import Categoria


# Create your views here.

def index(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias/index.html", {"categorias": categorias})

def create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias:index')
    else:

        form = CategoriaForm()

    return render(request, 'categorias/create.html', {'form': form})

def edit(request, pk):
    categorias = Categoria.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categorias)
        if form.is_valid():
            form.save()
            return redirect('categorias:index')
    else:
        form = CategoriaForm(instance=categorias)
    return render(request, 'categorias/edit.html', {'form': form, "categorias": categorias})

def delete(request, pk):
    categorias = Categoria.objects.get(id=pk)
    if request.method == 'POST':
        categorias.delete()
        return redirect('categorias:index')
    else:
        form = CategoriaForm(instance=categorias)
    return render(request, 'categorias/delete.html', {'form': form, "categorias": categorias})

def detail(request, pk):
    categorias = Categoria.objects.get(id=pk)
    return render(request, 'categorias/detail.html', {'categorias': categorias})
