from rest_framework import serializers

from categorias.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source="parent.name", read_only=True)

    class Meta:
        model = Categoria
        fields = [
            "id",
            "name",
            "parent",
            "parent_name",
            "is_subcategory",
        ]
        read_only_fields = ["id", "is_subcategory", "parent_name"]
