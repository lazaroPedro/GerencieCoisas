from rest_framework import serializers
from django.contrib.auth.models import User
from categorias.models import Categoria
from fornecedores.models import Fornecedor
from produtos.models import Produto
from movimentacoes.models import Movimentacao

class CategoriaSerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Categoria
        fields = ['id', 'name', 'parent', 'subcategories', 'is_subcategory']

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = Produto
        fields = [
            'id', 'name', 'description', 'price', 'quantity', 
            'active', 'category', 'category_name', 'supplier', 'created'
        ]

class MovimentacaoSerializer(serializers.ModelSerializer):
    usuario_name = serializers.ReadOnlyField(source='usuario.username')
    acao_display = serializers.CharField(source='get_acao_display', read_only=True)

    class Meta:
        model = Movimentacao
        fields = ['id', 'usuario', 'usuario_name', 'acao', 'acao_display', 'descricao', 'criado_em']