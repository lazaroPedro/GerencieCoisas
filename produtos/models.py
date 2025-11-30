from django.core.exceptions import ValidationError
from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(
        'categorias.Categoria',
        on_delete=models.PROTECT,
        verbose_name="Categoria",
        related_name="produtos"
    )
    supplier = models.ManyToManyField(
        'fornecedores.Fornecedor',
        verbose_name="Fornecedor",
        related_name="produtos"
    )
    def __str__(self):
        return self.name

    def clean(self):
        if self.category and not self.category.is_subcategory:
            raise ValidationError({
                'category': 'Produtos só podem ser associados a subcategorias.'
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)