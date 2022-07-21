from django.db import models
from hospedes.models import Hospede
from quartos.models import Quarto

# Create your models here.
class Hospedagem(models.Model):
    hospede = models.ForeignKey(Hospede, on_delete=models.DO_NOTHING)
    quarto = models.ForeignKey(Quarto, on_delete=models.DO_NOTHING)
    tipo = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
    )
    tipo_hospedagem = models.CharField(max_length=1, choices=tipo)

    def __str__(self):
        identificacao = ' '.join([str(self.id), str(self.hospede), str(self.quarto) ,self.tipo_hospedagem])
        return identificacao

    def save(self, *args, **kwargs):
        quarto = Quarto.objects.get(id=self.quarto_id)
        hospede = Hospede.objects.get(id=self.hospede_id)

        if self.tipo == 'E':
            hospedar = Quarto(
                id = quarto.id,
                tipo = quarto.tipo,
                hospede = hospede,
                status = 'O'
            )
            hospedar.save()
        elif self.tipo == 'S':
            hospedar = Quarto(
                id = quarto.id,
                tipo = quarto.tipo,
                hospede = None,
                status = 'L'
            )
            hospedar.save()
        return super(Hospedagem, self).save(*args, **kwargs)
    