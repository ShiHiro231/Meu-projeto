
# Importa funções para renderizar páginas e redirecionar
from django.shortcuts import render, redirect
# Importa função para verificar a senha
from django.contrib.auth.hashers import check_password
# Importa o modelo Administrador
from .models import Administrador

# Função responsável pelo login
def login(request):    
    # Verifica se o formulário foi enviado
    if request.method == "POST":
          # Pega o login digitado
        login_digitado = request.POST.get("login")
          # Pega a senha digitada
        senha_digitada = request.POST.get("senha")

        try:
            # Procura o administrador pelo login
            administrador = Administrador.objects.get(
                login=login_digitado
            )
            # Verifica se a senha está correta
            if check_password(senha_digitada, administrador.senha):
                # Guarda o ID do administrador na sessão
                request.session["admin_id"] = administrador.id
                # Vai para o painel
                return redirect("painel")

            else:
                #  mensagem de erro
                return render(
                    request,
                    "administrador/login.html",
                    {"erro": "Login ou senha incorretos."}
                )
        # Caso o login não seja encontrado
        except Administrador.DoesNotExist:
            # mensagem de erro
            return render(
                request,
                "administrador/login.html",
                {"erro": "Login ou senha incorretos."}
            )
        # mosttra a pagina de login
        return render(request, "administrador/login.html")
    
    

# Função responsável pelo painel
def painel(request):
    # Ve se o usuario esta logado
    if "admin_id" not in request.session:
        return redirect("login")
    # Busca o administrador pelo ID salvo na sessão
    administrador = Administrador.objects.get(
        id=request.session["admin_id"]
    )
    # mostra a pagina do painel
    return render(
        request,
        "administrador/painel.html",
        {"administrador": administrador}
    )
# Função que faz o logout
def logout(request):
    # finaliza a sessão
    request.session.flush()
    # Volta para o login de usuario
    return redirect("login")
