from django import forms
from .models import Evento

class LoginForm(forms.Form):
     username = forms.CharField(label='Usuário', max_length=150)
     password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class EventoForm(forms.ModelForm):
     class Meta:
          model = Evento
          fields = ['nome', 'descricao', 'hora_inicio', 'hora_fim', 'data', 'local']