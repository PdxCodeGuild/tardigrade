from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def authenticate(request):
#     return render(request, 'authenticate/authenticate.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Are Now Logged In!")
            return redirect('home')
        else:
            messages.success(request, "Login Error - Please Try Again...")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("🚢Logout Was Successful! Remember to Look Out for Anger Icebergs 🔭"))
    return redirect('home')