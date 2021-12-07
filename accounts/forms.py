from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Departamento

class Signupform(UserCreationForm):
    email = forms.EmailField(max_length=200)
    nome = forms.CharField(max_length=255)
    ano_de_ingresso = forms.IntegerField()
    departamento = forms.ModelChoiceField(queryset=Departamento.objects)
    data_de_nascimento = forms.DateField()

    class Meta:
        model = User
        fields = ('nome', 'email', 'ano_de_ingresso', 'departamento', 'username', 'password1', 'password2')
