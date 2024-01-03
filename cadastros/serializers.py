from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cadastros.models import Cidade


# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class CidadeSerializer(ModelSerializer):

    estado_nome = serializers.ReadOnlyField(source='estado.nome')
    # pais_nome = serializers.ReadOnlyField(source='estado.pais.nome')
    # estado = serializers.PrimaryKeyRelatedField(queryset=Cidade.objects.all())
    class Meta:
        model = Cidade
        fields = ['id', 'pais_nome', 'estado_nome', 'nome', 'capital', 'descricao']


