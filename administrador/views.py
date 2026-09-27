
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Administrador


def login(request):

    if request.method == "POST":

        login_digitado = request.POST.get("login")
        senha_digitada = request.POST.get("senha")

        try:
            administrador = Administrador.objects.get(
                login=login_digitado
            )

            if check_password(senha_digitada, administrador.senha):

                request.session["admin_id"] = administrador.id

                return redirect("painel")

            else:

                return render(
                    request,
                    "administrador/login.html",
                    {"erro": "Login ou senha incorretos."}
                )

        except Administrador.DoesNotExist:

            return render(
                request,
                "administrador/login.html",
                {"erro": "Login ou senha incorretos."}
            )


    return render(request, "administrador/login.html")


def painel(request):

    if "admin_id" not in request.session:
        return redirect("login")

    administrador = Administrador.objects.get(
        id=request.session["admin_id"]
    )

    return render(
        request,
        "administrador/painel.html",
        {"administrador": administrador}
    )
def logout(request):
    request.session.flush()

    return redirect("login")
