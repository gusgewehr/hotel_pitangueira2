from django import forms

class reservar(forms.Form):
    nome = forms.CharField(label='nome', max_length=100)
    sobrenome = forms.CharField(label='sobrenome', max_length=100)
    tipo_quarto = (
        (1, 'Simples'),
        (2, 'Casal'),
        (3, 'Suite Luxo'),
    )
    quarto = forms.ChoiceField(label='Quarto', choices=tipo_quarto)
    cpf = forms.CharField(label='cpf', max_length=11)
    numero_cartao = forms.CharField(label='Número do cartão de crédito', max_length=50)
    data_validade = forms.DateField(label='Data de validade')
    codigo_seguranca = forms.CharField(label='Código de Segurança', max_length=3)
