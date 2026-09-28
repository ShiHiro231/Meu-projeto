# Importa a função para criar URLs
from django.urls import path
# Importa as funções do arquivo views.py
from . import views

# Define as URLs do aplicativo
urlpatterns = [
    # URL para fazer login
    path("login/", views.login, name="login"),
    # URL para acessar o painel
    path("painel/", views.painel, name="painel"),
    # URL para sair da conta
    path("logout/", views.logout, name="logout")
    ]

