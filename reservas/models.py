from django.db import models

# Create your models here.
class Reserva(models.Model):
    class Tipo_quarto(models.IntegerChoices):
        Simples = 1
        Casal = 2
        Luxo = 3

    nome = models.CharField( max_length=100)
    sobrenome = models.CharField(max_length=100)
    quarto = models.IntegerField(choices=Tipo_quarto.choices)
    cpf = models.CharField(max_length=11)
    numero_cartao = models.CharField( max_length=50)
    data_validade = models.DateField()
    codigo_seguranca = models.CharField(max_length=3)

    def __str__(self):
        identificacao = ' '.join([str(self.id), str(self.nome), str(self.sobrenome) ,str(self.quarto)])
        return identificacao
