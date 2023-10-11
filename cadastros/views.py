from django.shortcuts import render, get_object_or_404

from cadastros.models import Cidade


# Create your views here.

# functions based views -> fbv
def lista_cidades(request):

    qs = Cidade.objects.all()  # qs = query set

    context = {
        'cidades': qs,
        'titulo': 'SIDIA'
    }

    return render(request, 'cadastros/lista_cidades.html', context)

def detalhe_cidades(request, id):

    #id_cidade = request.GET['id_cidade']
    #cidade = Cidade.objects.get(pk=id_cidade)
    cidade = get_object_or_404(Cidade, pk=id)
    context = {
        'cidade': cidade,
        'titulo': 'SIDIA'
    }

    return render(request, 'cadastros/detalhe_cidades.html', context)
