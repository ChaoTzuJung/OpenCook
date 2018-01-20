from django.shortcuts import render, redirect
from recipe.models import Recipe
from datetime import datetime, timedelta
# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

def get_index(request):
    title = "OpenCook"
    recipes = Recipe.objects.all()
    return render(request, 'index.html', locals())
    return response

def get_signup(request):
    return render(request, 'signup.html')

def post_signup(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    
    user = User.objects.create_user(username, email, password)
    if user:
        return redirect('/', locals())
    else:
        redirect('/signup', locals())
    return render(request, 'index.html')

def post_logout(request):
    auth.logout(request)
    return redirect('/')

def post_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/', locals())
    else:
        return redirect('/', locals())
