from django.urls import path
from django.contrib.auth import views as auth_views
# Importa as views dos novos arquivos
from .views import paginas, api 

urlpatterns = [
    # Autenticação Nativa
    path("login/", auth_views.LoginView.as_view(template_name="administrador/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    
    # Páginas (HTML)
    path("painel/", paginas.painel, name="painel"),
    path("calendario/", paginas.calendario, name="calendario"),
    
    # APIs (JSON)
    path("api/eventos/", api.api_eventos, name="api_eventos"),
    path("api/evento/salvar/", api.api_salvar_evento, name="api_salvar_evento"),
    path("api/evento/excluir/<int:evento_id>/", api.api_excluir_evento, name="api_excluir_evento"),
    path("api/publica/eventos/", api.api_eventos_publicos, name="api_eventos_publicos"),
]