from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EnderecoForm
from .models import Endereco
import requests, certifi

class Home(TemplateView):
    template_name = 'home.html'

def consulta_cep(request):
    form = EnderecoForm(request.GET or None)

    if form.is_valid():
        cep = form.cleaned_data['cep']
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json", verify=certifi.where())

        if response.status_code == 200:
            data = response.json()
            endereco = Endereco(
                cep = data.get('cep'),
                rua = data.get('logradouro'),
                bairro = data.get('bairro'),
                cidade = data.get('localidade'),
                estado = data.get('uf')
            )

            endereco.save()
            return render(request, 'endereco.html', {'endereco': endereco}) # Pegou o CEP com sucesso
    return render(request, 'endereco.html', {'endereco': 'CEP não existente na base de dados'}) # Se não conseguir pegar o CEP