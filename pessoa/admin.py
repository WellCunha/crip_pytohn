from django.contrib import admin
from .models import Pessoa
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'alcunha', 'data_nascimento', 'ativa',  ]
    search_fields = ['nome_completo', 'alcunha', 'data_nascimento', 'ativa', ]
    list_filter  = ['ativa', 'alcunha', 'data_nascimento',]
     
readonly_fild = ['ativa', ]
date_hierarchy = 'published_date',

admin.site.register(Pessoa, PessoaAdmin)