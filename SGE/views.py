from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento

#Imports Cadastro
from .forms import EventoForm

#Imports Login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def index(request):
    eventos = Evento.objects.all()
    return render(request, 'index.html', {'eventos': eventos})

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('')
            else:
                form.add_error(None, 'Usuário ou senha inválidos')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def cadEvento(request):
    sucesso = False
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
            form = EventoForm()
            return redirect('home')
    else:
        form = EventoForm()

    return render(request, 'cadEvento.html', {'form': form, 'sucesso': sucesso})

def listarEventos(request):
    eventos = Evento.objects.all()
    return render(request, 'listarEventos.html', {'eventos': eventos})

def excluirEvento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento.delete()
    return redirect('listarEventos')

def editarEvento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listarEventos')
    else:
        form = EventoForm(instance=evento)
    
    return render(request, 'cadEvento.html', {'form': form, 'editando': True})

    


    
