from dataclasses import fields
from datetime import date
from django import forms
from django.forms import fields, models
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'alcunha', 'data_nascimento', 'ativa', ]