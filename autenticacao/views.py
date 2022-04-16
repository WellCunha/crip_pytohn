from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

  
#Login

def logar(request):

   if request.user.is_authenticated:

    return redirect('/')

   if request.method == "GET":

    return render(request, 'logar.html')
   
   elif request.method == "POST":

    username = request.POST.get('username')
    senha =    request.POST.get('password')

    usuario = auth.authenticate(username = username, password = senha)

    if not usuario:

        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')

        return redirect('/auth/logar')

        
    else:

        auth.login(request, usuario)

        return redirect('home')

def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')

    
