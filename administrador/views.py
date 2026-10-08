# Importa funções para renderizar páginas e redirecionar
from django.shortcuts import render, redirect
# Importa função para verificar a senha
from django.contrib.auth.hashers import check_password
from django.utils import timezone
from datetime import timedelta
# Importa o modelo Administrador
from .models import Administrador


# Função responsável pelo login
def login(request):
    # Verifica se o formulário foi enviado
    if request.method == "POST":

        tentativas = request.session.get("tentativas", 0)

        if tentativas >= 5:
            bloqueio_ate = request.session.get("bloqueio_ate")
            if bloqueio_ate:
                if timezone.now().timestamp() < bloqueio_ate:
                    return render(
                        request,
                        "administrador/login.html",
                        {"erro": "Seu acesso foi bloqueado temporariamente. Tente novamente mais tarde."}
                    )
                request.session["tentativas"] = 0
                request.session["bloqueio_ate"] = None
                tentativas = 0

        # Pega o login digitado
        login_digitado = request.POST.get("login")
        # Pega a senha digitada
        senha_digitada = request.POST.get("senha")

        try:
            # Procura o administrador pelo login
            administrador = Administrador.objects.get(login=login_digitado)
            # Verifica se a senha está correta
            if check_password(senha_digitada, administrador.senha):
                request.session["tentativas"] = 0
                request.session["bloqueio_ate"] = None
                # Guarda o ID do administrador na sessão
                request.session["admin_id"] = administrador.id
                # Vai para o painel
                return redirect("painel")
            else:
                request.session["tentativas"] = tentativas + 1

                if tentativas + 1 >= 5:
                    request.session["bloqueio_ate"] = (timezone.now() + timedelta(minutes=5)).timestamp()

                # Mensagem de erro
                return render(
                    request,
                    "administrador/login.html",
                    {"erro": "Login ou senha incorretos."}
                )
        # Caso o login não seja encontrado
        except Administrador.DoesNotExist:
            request.session["tentativas"] = tentativas + 1
            if tentativas + 1 >= 5:
                request.session["bloqueio_ate"] = (timezone.now() + timedelta(minutes=5)).timestamp()
            # Mensagem de erro
            return render(
                request,
                "administrador/login.html",
                {"erro": "Login ou senha incorretos."}
            )

    # ✅ Return final — atende requisições GET (quando o usuário só abre a página) estava faltando isso no codigo.
    return render(request, "administrador/login.html")


# Função responsável pelo painel
def painel(request):
    # Verifica se o usuário está logado
    if "admin_id" not in request.session:
        return redirect("login")
    # Busca o administrador pelo ID salvo na sessão
    administrador = Administrador.objects.get(id=request.session["admin_id"])
    # Mostra a página do painel
    return render(
        request,
        "administrador/painel.html",
        {"administrador": administrador}
    )


# Função que faz o logout
def logout(request):
    # Finaliza a sessão
    request.session.flush()
    # Volta para o login de usuário
    return redirect("login")

# Função responsável pelo calendário heheh
def calendario(request):
    # Verifica se o usuário está logado
    if "admin_id" not in request.session:
        return redirect("login")
    # Busca o administrador pelo ID salvo na sessão
    administrador = Administrador.objects.get(id=request.session["admin_id"])
    # Mostra a página do calendário
    return render(
        request,
        "administrador/calendario.html",
        {"administrador": administrador}
    )

# ============================================
# APIs DO CALENDÁRIO
# ============================================
import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .models import Evento


@require_GET
def api_eventos(request):
    """Retorna todos os eventos em JSON."""
    if "admin_id" not in request.session:
        return JsonResponse({"erro": "Não autorizado"}, status=403)

    eventos = Evento.objects.all()
    lista = []
    for e in eventos:
        lista.append({
            "id": e.id,
            "nome_evento": e.nome_evento,
            "descricao": e.descricao or "",
            "data": e.data.isoformat(),
            "horario_inicio": e.horario_inicio.strftime("%H:%M") if e.horario_inicio else "",
            "horario_fim": e.horario_fim.strftime("%H:%M") if e.horario_fim else "",
            "aceita_doacao": e.aceita_doacao,
            "aceita_voluntariado": e.aceita_voluntariado,
        })
    return JsonResponse(lista, safe=False)


@require_POST
def api_salvar_evento(request):
    """Cria ou atualiza um evento."""
    if "admin_id" not in request.session:
        return JsonResponse({"erro": "Não autorizado"}, status=403)

    try:
        dados = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"erro": "JSON inválido"}, status=400)

    evento_id = dados.get("id")

    if evento_id:
        try:
            evento = Evento.objects.get(pk=evento_id)
        except Evento.DoesNotExist:
            return JsonResponse({"erro": "Evento não encontrado"}, status=404)
    else:
        evento = Evento()

    evento.nome_evento = dados.get("nome_evento", "").strip()
    evento.descricao = dados.get("descricao", "").strip()
    evento.data = dados.get("data")
    evento.horario_inicio = dados.get("horario_inicio") or None
    evento.horario_fim = dados.get("horario_fim") or None
    evento.aceita_doacao = bool(dados.get("aceita_doacao", False))
    evento.aceita_voluntariado = bool(dados.get("aceita_voluntariado", False))

    if not evento.nome_evento or not evento.data:
        return JsonResponse({"erro": "Nome e data são obrigatórios"}, status=400)

    evento.save()

    return JsonResponse({
        "status": "ok",
        "id": evento.id,
        "nome_evento": evento.nome_evento,
    })


@require_POST
def api_excluir_evento(request, evento_id):
    """Exclui um evento."""
    if "admin_id" not in request.session:
        return JsonResponse({"erro": "Não autorizado"}, status=403)

    try:
        evento = Evento.objects.get(pk=evento_id)
        evento.delete()
        return JsonResponse({"status": "ok"})
    except Evento.DoesNotExist:
        return JsonResponse({"erro": "Evento não encontrado"}, status=404)