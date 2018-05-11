from django.shortcuts import render, redirect, render_to_response
from django.utils import timezone
from .models import Transuser
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect


def home_page(request):
    me = request.user
    print(Transuser.objects.all)
    return render(request, 'transfer/home.html', {'me': me})

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('qiwiwallet', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('transfer/home.html', args)