import json
from datetime import date
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from ..models import Evento # Note os dois pontos (..) para voltar uma pasta

@require_GET
@login_required(login_url='login')
def api_eventos(request):
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
@login_required(login_url='login')
def api_salvar_evento(request):
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
    return JsonResponse({"status": "ok", "id": evento.id, "nome_evento": evento.nome_evento})

@require_POST
@login_required(login_url='login')
def api_excluir_evento(request, evento_id):
    try:
        evento = Evento.objects.get(pk=evento_id)
        evento.delete()
        return JsonResponse({"status": "ok"})
    except Evento.DoesNotExist:
        return JsonResponse({"erro": "Evento não encontrado"}, status=404)

@require_GET
def api_eventos_publicos(request):
    eventos = Evento.objects.filter(data__gte=date.today()).order_by('data', 'horario_inicio')
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