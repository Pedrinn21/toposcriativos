from django.db import models
from tipoproduto.models import TipoProduto
from materiaprima.models import MateriaPrima

class Produto(models.Model):
    fktipoproduto = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    materiaprima = models.ManyToManyField(MateriaPrima, related_name="produtos")
    gasto = models.FloatField()
    valor = models.FloatField()
    
    
