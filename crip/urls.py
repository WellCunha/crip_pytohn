from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('', include('main.urls')),
    path('pessoas/', include('pessoa.urls')),
]
