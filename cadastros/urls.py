from django.urls import include, path

from cadastros.views import lista_cidades, detalhe_cidades

urlpatterns = [
    path('', lista_cidades, name='cidade-list'),
    path('detalhe/<int:id>/', detalhe_cidades, name='cidades-detalhe')
]
