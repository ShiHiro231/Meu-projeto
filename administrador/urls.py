# Importa a função para criar urls
from django.urls import path
# Importa as funções do views.py
from . import views

# Define as urrls do aplicativo
urlpatterns = [
    # url para fazer login
    path("login/", views.login, name="login"),
    # url para acessar o painel
    path("painel/", views.painel, name="painel"),
    # url para sair da conta
    path("logout/", views.logout, name="logout")
    ]

