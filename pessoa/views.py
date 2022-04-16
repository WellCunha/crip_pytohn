from pyexpat import model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Pessoa
from .forms import PessoaForm

class ListaPessoaView(ListView):

    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

    class PessoaUpdateView(UpdateView):
        model = Pessoa
       

