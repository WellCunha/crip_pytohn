from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.


class HomeView(TemplateView):
    template_name = 'main/index.html'
