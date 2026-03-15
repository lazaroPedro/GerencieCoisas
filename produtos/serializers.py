from rest_framework import serializers

from categorias.models import Categoria
from fornecedores.models import Fornecedor
from produtos.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    supplier_names = serializers.StringRelatedField(source="supplier", many=True, read_only=True)
    supplier = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Fornecedor.objects.all()
    )
    category = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta:
        model = Produto
        fields = [
            "id",
            "name",
            "description",
            "price",
            "active",
            "created",
            "updated",
            "quantity",
            "category",
            "category_name",
            "supplier",
            "supplier_names",
        ]
        read_only_fields = ["id", "created", "updated", "category_name", "supplier_names"]

    def validate_category(self, value):
        if not value.is_subcategory:
            raise serializers.ValidationError(
                "Produtos só podem ser associados a subcategorias."
            )
        return value
