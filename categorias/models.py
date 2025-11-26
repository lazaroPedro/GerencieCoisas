from django.db import models

# Create your models here.

class Categoria(models.Model):

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories',
        verbose_name='Categoria Pai'
    )
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome")

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} > {self.name}"
        return self.name

    @property
    def is_subcategory(self):
        return self.parent is not None
