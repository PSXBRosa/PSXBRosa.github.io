from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        user_first_name = request.POST['first_name']
        user_last_name = request.POST['last_name']
        user_email = request.POST['email']
        user_username = request.POST['username']
        user_password = request.POST['password']
        user = User.objects.create_user(username=user_username,password=user_password,email=user_email,first_name=user_first_name,last_name=user_last_name)
        user.save()
        return HttpResponseRedirect(reverse('list'))
    else:
        return render(request, 'cadastro.html', {})