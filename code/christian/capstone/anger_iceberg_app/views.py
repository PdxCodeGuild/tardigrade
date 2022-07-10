from django.http import HttpResponse
from django.shortcuts import render, redirect 



### DONT FORGET - You'll need to eventually import your class name

# Create your views here.

def home(request):
    return render(request, "home.html")
