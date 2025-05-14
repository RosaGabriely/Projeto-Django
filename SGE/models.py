from django.db import models
from django import forms

class Local(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Evento(models.Model):
        nome = models.CharField(max_length=255)
        descricao = models.TextField(max_length=80)
        data = models.DateField()
        horaInicio = models.TimeField()
        horaFim = models.TimeField()
        local = models.CharField(max_length=100)
    
class Participante(models.Model):
     nome = models.CharField(max_length=255)
     email = models.EmailField()
     telefone = models.CharField(max_length=20)

class Inscricao(models.Model):
     evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
     participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
     local = models.ForeignKey(Local, on_delete=models.CASCADE)
     data_inscricao = models.DateTimeField(auto_now_add=True)

class LoginForm(forms.Form):
     username = forms.CharField(label='Usuário', max_length=150)
     password = forms.CharField(label='Senha', widget=forms.PasswordInput)
        
    

