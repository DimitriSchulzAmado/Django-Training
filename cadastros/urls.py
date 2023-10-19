from django.urls import include, path

from cadastros.views import lista_cidades, detalhe_cidade, cadastra_cidade, delete_cidade, update_cidade

urlpatterns = [
    path('', lista_cidades, name='cidades-list'),
    path('detalhe/<int:id>/', detalhe_cidade, name='cidades-detalhe'),
    path('delete/<int:id>/', delete_cidade, name='cidades-delete'),
    path('update/<int:id>/', update_cidade, name='cidades-update'),
    path('create/', cadastra_cidade, name='cidades-cadastro')
]
