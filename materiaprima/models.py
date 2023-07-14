from django.db import models
from tipopapel.models import TipoPapel

class MateriaPrima(models.Model):
    fktipopapel = models.ForeignKey(TipoPapel, on_delete=models.CASCADE)
    gramatura = models.FloatField()
    quantidade = models.IntegerField()
    
    
