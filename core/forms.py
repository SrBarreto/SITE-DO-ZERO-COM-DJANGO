from django import forms
from .models import Imagem, Projeto

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['nome', 'arquivo']

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'link', 'imagem']