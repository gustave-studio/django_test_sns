from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some':100})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーはすでに登録されています。'})
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login.html', {'context':'loged in'})
        else:
            return render(request, 'login.html', {'context':'not loged in'})
    return render(request, 'login.html', {'context':'get method'})