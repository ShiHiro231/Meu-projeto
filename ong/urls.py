# Importa o painel administrativo do Django
from django.contrib import admin
# Importa as funções para criar URLs
from django.urls import path, include
# Adicionando a capacidade de renderizar templates diretamente
from django.views.generic import TemplateView

# Define as URLs do projeto
urlpatterns = [
    # URL do painel administrativo
    path('admin/', admin.site.urls),
    # Inclui as URLs do aplicativo administrador
    path("administrador/", include("administrador.urls")),
    # Rota da página principal do site público, renderizando o template 'home.html'
    path('', TemplateView.as_view(template_name='site_publico/home.html'), name='home_publica'),

    # Rota da página de pagamento e voluntário renderizando o template 'pagamento.html'
    path('', TemplateView.as_view(template_name='site_publico/home.html'), name='home_publica'),
    path('pagamento/', TemplateView.as_view(template_name='site_publico/pagamento.html'), name='pagamento'),
    path('voluntario/', TemplateView.as_view(template_name='site_publico/voluntario.html'), name='voluntario'),
]
