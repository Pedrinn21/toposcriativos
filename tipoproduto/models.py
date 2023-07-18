from django.db import models

class TipoProduto(models.Model):
    descricao = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.descricao