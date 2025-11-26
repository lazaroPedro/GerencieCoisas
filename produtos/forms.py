from django import forms

from categorias.models import Categoria
from produtos.models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['name', 'description', 'price', 'quantity', 'active', 'category', 'supplier']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'price': 'Preço (R$)',
            'quantity': 'Quantidade Inicial',
            'active': 'Produto Ativo?',
            'category': 'Categoria',
            'supplier': 'Fornecedores'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Categoria.objects.filter(parent__isnull=False)


class ProdutoEditForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['name', 'description', 'price', 'active', 'category', 'supplier']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'price': 'Preço (R$)',
            'active': 'Produto Ativo?',
            'category': 'Categoria',
            'supplier': 'Fornecedores'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Categoria.objects.filter(parent__isnull=False)