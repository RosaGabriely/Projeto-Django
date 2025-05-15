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
from SGE.views import index, loginView, cadEvento, excluirEvento,editarEvento,listarEventos, cadParticipante, listarParticipante,excluirParticipante,editarParticipante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginView, name='login'),
    path('home', index, name='home'),
    path('cadastro/', cadEvento, name='cadEvento'),
    path('excluir/<int:id>/', excluirEvento, name='excluirEvento'),
    path('editar/<int:id>/', editarEvento, name='editarEvento'),
    path('listarEventos', listarEventos, name='listarEventos'),
    path('cadastroParticipante/', cadParticipante, name='cadParticipante'),
    path('listarParticipante',listarParticipante, name='listarParticipante'),
    path('excluir/<int:id>/', excluirParticipante, name='excluirParticipante'),
    path('editar/<int:id>/', editarParticipante, name='editarParticipante'),
    

]


