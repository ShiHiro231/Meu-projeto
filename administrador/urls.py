# Importa a função para criar urls
from django.urls import path
# Importa as funções do views.py
from . import views

# Define as urls do aplicativo
urlpatterns = [
    # url para fazer login
    path("login/", views.login, name="login"),
    # url para acessar o painel
    path("painel/", views.painel, name="painel"),
    # url para sair da conta
    path("logout/", views.logout, name="logout"),
    # url do calendário
    path("calendario/", views.calendario, name="calendario"),

    # APIs do calendário (JSON)
    path("api/eventos/", views.api_eventos, name="api_eventos"),
    path("api/evento/salvar/", views.api_salvar_evento, name="api_salvar_evento"),
    path("api/evento/excluir/<int:evento_id>/", views.api_excluir_evento, name="api_excluir_evento"),
]