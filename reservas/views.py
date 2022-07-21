from django.shortcuts import render
from .forms import reservar
from .models import Reserva

# Create your views here.
def reservas(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = reservar(request.POST)
        # check whether it's valid:
        if form.is_valid():
            reserva = Reserva(
                nome = form.cleaned_data['nome'],
                sobrenome = form.cleaned_data['sobrenome'],
                quarto = form.cleaned_data['quarto'],
                cpf = form.cleaned_data['cpf'],
                numero_cartao = form.cleaned_data['numero_cartao'],
                data_validade = form.cleaned_data['data_validade'],
                codigo_seguranca = form.cleaned_data['codigo_seguranca'],
                )
            reserva.save()
            return render(request, 'obrigado.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = reservar()    
        return render(request, 'index.html', {'form':form})