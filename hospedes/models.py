from django.db import models

# Create your models here.
class Hospede(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome