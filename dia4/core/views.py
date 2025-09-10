from django.views.generic import FormView, ListView, DeleteView, DetailView
import requests
import certifi
from .forms import EnderecoForm
from .models import Endereco

class ViaCepFormView(FormView):
    template_name = 'endereco.html'
    form_class = EnderecoForm
    success_url = '.'  # redireciona para a mesma página

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json", verify=certifi.where())

        if response.status_code == 200:
            data = response.json()
            endereco = Endereco(
                cep=data.get('cep'),
                rua=data.get('logradouro'),
                bairro=data.get('bairro'),
                cidade=data.get('localidade'),
                estado=data.get('uf')
            )
            endereco.save()
            return self.render_to_response(self.get_context_data(form=form, endereco=endereco))
        else:
            msg = 'CEP não existente na base de dados'
            return self.render_to_response(self.get_context_data(form=form, endereco=msg))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class ViaCepListView(ListView):
    model = Endereco
    paginate_by = 10
    template_name = 'listagem.html'
    context_object_name = 'enderecos'

class ViaCepDeleteView(DeleteView):
    pass

class ViaCepDetailView(DetailView):
    pass