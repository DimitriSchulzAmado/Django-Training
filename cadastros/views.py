from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

from cadastros.models import Cidade
from cadastros.templates.forms import CidadeForm


# Create your views here.

# functions based views -> fbv
def lista_cidades(request):

    qs = Cidade.objects.all().order_by('nome')  # qs -> query set

    context = {
        'cidades': qs,
        'titulo': 'SIDIA'
    }

    return render(request, 'cadastros/lista_cidades.html', context)


def detalhe_cidade(request, id):

    #id_cidade = request.GET['id_cidade']
    #cidade = Cidade.objects.get(pk=id_cidade)
    cidade = get_object_or_404(Cidade, pk=id)
    context = {
        'cidade': cidade,
        'titulo': 'SIDIA'
    }

    return render(request, 'cadastros/detalhe_cidades.html', context)


# Create
@login_required
def cadastra_cidade(request):

    if request.method == 'POST':
        form = CidadeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cidades-list')
    else:
        form = CidadeForm()

    context = {
        'form': form,
        'titulo':'SIDIA'
    }
    return render(request, 'cadastros/cadastra_cidades.html', context)


@login_required
def update_cidade(request, id):

    cidade_obj = get_object_or_404(Cidade, pk=id)
    form = CidadeForm(request.POST or None, instance=cidade_obj)

    if request.method == 'POST':
        # Receber os dados "editados" e salvar
        form = CidadeForm(request.POST, instance=cidade_obj)
        if form.is_valid():
            form.save()
            return redirect('cidades-list')

    context = {
        'form': form,
        'obj': cidade_obj
    }

    return render(request, 'cadastros/update_cidades.html', context)


@login_required
def delete_cidade(request, id):

    cidade = get_object_or_404(Cidade, pk=id)
    cidade.delete()

    return redirect('cidades-list')
