from django import forms
from cadastros.models import Cidade


class CidadeForm(forms.ModelForm):

    class Meta:
        model = Cidade
        #fields = ['nome', 'capital']
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data['nome']

        if name == '':
            raise ValidationError('')