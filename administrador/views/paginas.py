from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from urllib.parse import quote
from ..forms import UserForm
from ..models import Evento

@login_required(login_url='login')
def painel(request):
    return render(request, "administrador/painel.html")

@login_required(login_url='login')
def calendario(request):
    return render(request, "administrador/calendario.html")

def voluntario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['usuario']
            telefone = form.cleaned_data['telefone']
            # Pega o valor do evento e o front tiver colocado no select
            evento_id = request.POST.get('evento')
            nome_evento = "Geral"  # Valor padrão caso não seja encontrado
            if evento_id:
                try:
                    ev= Evento.objects.get(id=evento_id)
                    nome_evento = ev.nome_evento
                except Evento.DoesNotExist:
                    pass
            
            # Cria a mensagem para o WhatsApp
            texto = f"Olá! Meu nome é {nome}, telefone {telefone}. Quero me voluntariar no evento: {nome_evento}."
            texto_url = quote(texto)
            
            # Substitua pelo número real da ONG(Joyce)
            numero_ong = "5511999999999" 
            return redirect(f"https://wa.me/{numero_ong}?text={texto_url}")
    else:
        form = UserForm()
    
    # Se for GET (só abrir a página), mostra o HTML
    return render(request, 'site_publico/voluntario.html', {'form': form})