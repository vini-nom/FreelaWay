from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def cadastro(request):

    #Renderização da página usando GET
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/Plataforma')
        return render(request, 'cadastro.html')

    elif request.method == 'POST':
     username = request.POST.get('username')
     senha = request.POST.get('password')
     confirma_senha = request.POST.get('confirm-password')
     print(f'{username} | {senha} | {confirma_senha}')

     if not senha == confirma_senha:
         messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
         return redirect('/auth/cadastro')

     if len(username.strip()) == 0 and len(senha.strip()) == 0:
         messages.add_message(request, constants.ERROR, 'Preencha todos os campos do formulário')
         return redirect('/auth/cadastro')

     user = User.objects.filter(username = username)

     if user.exists():
         messages.add_message(request, constants.ERROR, 'Conta já existente')
         return redirect('/auth/cadastro')

     try:

       user = User.objects.create_user(username = username, password = senha)
       user.save()

       return redirect('/auth/login')

     except:
         messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
         return redirect('/auth/cadastro')

     if request.user.is_authenticated:
         return redirect('/UsuarioJaLogado')

     return HttpResponse('Recebido')



def logar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/Plataforma')
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        user = auth.authenticate(username = username, password = senha)

        if len(username.strip()) == 0 and len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos do login para entrar')
            return redirect('/auth/login')

        if not user:
            messages.add_message(request, constants.ERROR, 'Senha ou Nome inválidos')
            return redirect('/auth/login')
        else:
            auth.login(request, user)
            return redirect('/jobs/encontrar_jobs')

        if request.user.is_authenticated:
            return redirect('/UsuarioJaLogado')

        return HttpResponse('Recebido')

def sair(request):
     auth.logout(request)
     return redirect('/auth/login')



