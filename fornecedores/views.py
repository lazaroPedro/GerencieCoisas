from django.shortcuts import render, redirect

from fornecedores.forms import FornecedorForm
from fornecedores.models import Fornecedor


# Create your views here.
def index(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "fornecedores/index.html", {"fornecedores": fornecedores})

def create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:index')
    else:
        form = FornecedorForm()

    return render(request, 'fornecedores/create.html', {'form': form})

def edit(request, pk):
    fornecedor = Fornecedor.objects.get(id=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:index')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedores/edit.html', {'form': form, 'fornecedor': fornecedor})

def delete(request, pk):
    fornecedor = Fornecedor.objects.get(id=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('fornecedores:index')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedores/delete.html', {'form': form, 'fornecedor': fornecedor})
