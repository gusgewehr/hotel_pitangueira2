from django.contrib import admin

# Register your models here.
from .models import Consumo, Tipo_Consumo


admin.site.register(Tipo_Consumo)

admin.site.register(Consumo)