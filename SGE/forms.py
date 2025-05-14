from django import forms
from .models import Evento

class LoginForm(forms.Form):
     email = forms.CharField(label='Usuário', max_length=150)
     password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class EventoForm(forms.ModelForm):
     class Meta:
          model = Evento
          fields = ['nome', 'descricao', 'horaInicio', 'horaFim', 'data', 'local'] 
          widgets = {
            'horaInicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'horaFim': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }