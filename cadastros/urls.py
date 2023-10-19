from django.contrib.auth.decorators import login_required
from django.urls import path

from cadastros.views import CidadeList, CidadeDetail, CidadeDelete, CidadeRegister, CidadeUpdate

urlpatterns = [
    path('', CidadeList.as_view(), name='cidades-list'),
    path('detalhe/<int:pk>/', CidadeDetail.as_view(), name='cidades-detalhe'),
    path('delete/<int:pk>/', login_required(CidadeDelete.as_view()), name='cidades-delete'),
    path('update/<int:pk>/', login_required(CidadeUpdate.as_view()), name='cidades-update'),
    path('create/', login_required(CidadeRegister.as_view()), name='cidades-cadastro')
]
