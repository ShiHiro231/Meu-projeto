# Importa o painel administrativo do Django
from django.contrib import admin
# Importa as funções para criar URLs
from django.urls import path, include

# Define as URLs do projeto
urlpatterns = [
    # URL do painel administrativo
    path('admin/', admin.site.urls),
    # Inclui as URLs do aplicativo administrador
    path("administrador/", include("administrador.urls")),
    
]
