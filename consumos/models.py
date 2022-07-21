from django.db import models
from hospedagens.models import Hospedagem

# Create your models here.
class Tipo_Consumo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=4000)


class Consumo(models.Model):
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_Consumo, on_delete=models.PROTECT)
    preco = models.DecimalField(decimal_places=2, max_digits=6)
    status_choices = (
        ('P', 'Pago'),
        ('A', 'Aberto'),
        ('C', 'Cancelado'),
    )
    status = models.CharField(max_length=1, choices=status_choices)