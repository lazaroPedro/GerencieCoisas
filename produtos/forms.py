from django import forms

from produtos.models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['name', 'description', 'price', 'quantity', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'price': 'Preço (R$)',
            'quantity': 'Quantidade Inicial',
            'active': 'Produto Ativo?'
        }

class ProdutoEditForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['name', 'description', 'price', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'price': 'Preço (R$)',
            'active': 'Produto Ativo?'
        }