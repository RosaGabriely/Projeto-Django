from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import ParticipanteForm
from .models import Participante
from .forms import Localform
from .models import Local
from django.contrib.auth import logout

#Imports Cadastro
from .forms import EventoForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import ParticipanteForm
from .models import Participante
from .forms import Localform
from .models import Local
from django.contrib.auth import logout

#Imports Cadastro
from .forms import EventoForm

#Imports Login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



def inicio(request):
    return render(request, 'telaPrincipal.html')

def registerView(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()

    return render(request, 'registro.html', {'user_form': user_form})


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('inicio')
        else:
                LoginForm = AuthenticationForm()
    else:
        LoginForm = AuthenticationForm()
    return render(request, 'login.html', {'LoginForm': LoginForm})

def cadEvento(request):
    sucesso = False
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
            form = EventoForm()
            return redirect('listarEventos')
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


        ##### PARTICIPANTE 
def cadParticipante(request):
    sucesso = False
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
            return redirect('listarParticipante')
    else:
            form = ParticipanteForm()

    return render(request, 'cadParticipante.html', {'form': form, 'sucesso': sucesso})
    
def listarParticipante(request):
    participantes = Participante.objects.all()
    return render(request, 'listarParticipante.html', {'participantes': participantes})

def excluirParticipante(request, id):
    participante = get_object_or_404(Participante, id=id)
    participante.delete()
    return redirect('listarParticipante')

def editarParticipante(request, id):
    participante = get_object_or_404(Participante, id=id)
    if request.method == 'POST':
        form = ParticipanteForm(request.POST, instance=participante)
        if form.is_valid():
            form.save()
            return redirect('listarParticipante')
    else:
        form = ParticipanteForm(instance=participante)
    
    return render(request, 'cadParticipante.html', {'form': form, 'editando': True})


  ##### LOCAL

def cadLocal(request):
    sucesso = False
    if request.method == 'POST':
        form = Localform(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
            return redirect('listarLocal')
    else:
        form = Localform()

    return render(request, 'cadLocal.html', {'form': form, 'sucesso': sucesso})
    

def listarLocal(request):
    locais = Local.objects.all()
    return render(request, 'listarLocal.html', {'locais' : locais})

def excluirLocal(request, id):
    local = get_object_or_404(Local, id=id)
    local.delete()
    return redirect('listarLocal')

def editarLocal(request, id):
    local = get_object_or_404(Local, id = id)
    if request.method == 'POST':
        form = Localform(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return redirect('listarLocal')
    else:
        form = Localform(instance=local)

    return render(request, 'cadLocal.html', {'form':form, 'editando': True})

#logout NavBar

def logoutView(request):
    logout(request)
    return redirect('login')
