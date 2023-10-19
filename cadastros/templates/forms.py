from django import forms
from django.core.exceptions import ValidationError

from cadastros.models import Cidade


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        # fields = ['nome', 'capital']
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data['nome']

        if name == 'Itajuba':
            raise ValidationError('Não pode')
