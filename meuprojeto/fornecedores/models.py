from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=70, null=False)
    codigo = models.IntegerField()
    ativo = models.BooleanField()
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
