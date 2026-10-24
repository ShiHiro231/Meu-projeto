from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def painel(request):
    return render(request, "administrador/painel.html")

@login_required(login_url='login')
def calendario(request):
    return render(request, "administrador/calendario.html")