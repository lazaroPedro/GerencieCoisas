from django.db import models

class Fornecedor(models.Model):
    name = models.CharField("Nome Fantasia", max_length=100)
    corporate_name = models.CharField("Razão Social", max_length=100)
    cnpj = models.CharField("CNPJ", max_length=20, unique=True)
    email = models.EmailField("Email")
    phone = models.CharField("Telefone", max_length=20)
    created = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return f"{self.name} ({self.cnpj})"

