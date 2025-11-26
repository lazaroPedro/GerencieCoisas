from django import forms

from categorias.models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['parent', 'name']
        widgets = {
            'parent': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Smartphones, Limpeza Pesada'})
        }
        labels = {
            'parent': 'Categoria Pai (Deixe vazio se for uma categoria principal)',
            'name': 'Nome da Categoria/Subcategoria',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = Categoria.objects.filter(parent__isnull=True)

