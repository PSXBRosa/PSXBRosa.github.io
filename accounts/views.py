from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Signupform

def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = Signupform()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)