"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SGE.views import ( 
    inicio, loginView, cadEvento, excluirEvento, editarEvento,listarEventos,
    cadParticipante, listarParticipante, excluirParticipante, editarParticipante,
    cadLocal, excluirLocal, editarLocal, listarLocal,
    logoutView, registerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginView, name='login'),
    path('inicio', inicio, name='inicio'),
    path('registro/', registerView, name="registerView"),

    #Eventos
    path('cadastro/', cadEvento, name='cadEvento'),
    path('excluir/<int:id>/', excluirEvento, name='excluirEvento'),
    path('editar/<int:id>/', editarEvento, name='editarEvento'),
    path('listarEventos', listarEventos, name='listarEventos'),

    #Participantes
    path('cadastroParticipante/', cadParticipante, name='cadParticipante'),
    path('excluirPart/<int:id>/', excluirParticipante, name='excluirParticipante'),
    path('editarPart/<int:id>/', editarParticipante, name='editarParticipante'),
    path('listarParticipante',listarParticipante, name='listarParticipante'),

    #Local
    path('cadLocal', cadLocal, name='cadLocal'),
    path('excluirLocal/<int:id>/', excluirLocal, name='excluirLocal'),
    path('editarLocal/<int:id>/', editarLocal, name='editarLocal'),
    path('listarLocal', listarLocal, name='listarLocal'),
    
    #NavBar
    path('logout/', logoutView, name='logout'),

]


