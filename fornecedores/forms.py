from django import forms
from fornecedores.models import Fornecedor


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['name', 'corporate_name', 'cnpj', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Distribuidora '}),
            'corporate_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00.000.000/0000-00'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nome Fantasia',
            'corporate_name': 'Razão Social',
            'cnpj': 'CNPJ',
            'email': 'E-mail de Contato',
            'phone': 'Telefone',
        }