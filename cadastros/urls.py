from django.urls import include, path

from cadastros.views import lista_cidades, detalhe_cidades, cadastra_cidade, delete_cidade

urlpatterns = [
    path('', lista_cidades, name='cidade-list'),
    path('detalhe/<int:id>/', detalhe_cidades, name='cidades-detalhe'),
    path('delete/<int:id>', delete_cidade, name='delete-cidade'),
    path('create/', cadastra_cidade, name='cidades-cadastro')
]
