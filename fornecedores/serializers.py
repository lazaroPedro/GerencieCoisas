from rest_framework import serializers

from fornecedores.models import Fornecedor


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = [
            "id",
            "name",
            "corporate_name",
            "cnpj",
            "email",
            "phone",
            "created",
        ]
        read_only_fields = ["id", "created"]
