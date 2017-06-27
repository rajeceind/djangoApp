# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm

# Create your views here.
def home(request):
	return render(request, 'blr/home.html', {})

def register(request):
	form = UserForm(request.POST or none)


	return render(request, 'registration.html', {"form" : form})


def login_user(request):
	if request.method == "POST":
	        username = request.POST['username']
	        password = request.POST['password']
	        user = authenticate(username=username, password=password)
	        if user is not None:
	            if user.is_active:
	                login(request, user)
	                return render(request, 'blr/add.html', {})
	            else:
	                return render(request, 'blr/login.html', {'error_message': 'Your account has been disabled'})
	        else:
	            return render(request, 'blr/login.html', {'error_message': 'Invalid login'})

	return render(request, 'blr/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('blr:login')



@login_required(login_url='/login/')
def add_items(request):
	return render(request, 'blr/add.html', {})



