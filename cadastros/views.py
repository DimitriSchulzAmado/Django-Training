from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from cadastros.models import Cidade
from cadastros.templates.forms import CidadeForm


class SidiaBaseListView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'INATEL'
        return context


class CidadeList(SidiaBaseListView):
    context_object_name = "cidades"
    queryset = Cidade.objects.order_by('nome')
    template_name = "cadastros/lista_cidades.html"


class CidadeDetail(DetailView):

    context_object_name = 'cidade'
    queryset = Cidade.objects.all()
    template_name = 'cadastros/detalhe_cidades.html'


class CidadeDelete(DeleteView):
    context_object_name = 'cidade'
    model = Cidade
    template_name = 'cadastros/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeRegister(CreateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastros/cadastra_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeUpdate(UpdateView, SuccessMessageMixin):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastros/update_cidades.html'
    success_url = reverse_lazy('cidades-list')
    success_message = 'Success to update register!'
