from django.db import models
from hospedes.models import Hospede

# Create your models here.
class Quarto(models.Model):
    class Tipo_quarto(models.IntegerChoices):
        Simples = 1
        Casal = 2
        Luxo = 3

    tipo = models.IntegerField(choices=Tipo_quarto.choices)
    hospede = models.ForeignKey(Hospede, on_delete=models.PROTECT, null=True, blank=True)
    status_choices = (
        ('O', 'Ocupado'),
        ('L', 'Livre'),
        ('R', 'Reservado'),
    )
    status = models.CharField(max_length=1, choices=status_choices)

    def __str__(self):
        identificacao = ' '.join(['Quarto', str(self.id), str(self.tipo), self.status])
        return identificacao

