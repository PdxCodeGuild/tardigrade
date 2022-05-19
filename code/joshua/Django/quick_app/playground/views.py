from django.shortcuts import render
from django.http import HttpResponse 


def home(request):

    return render(request, 'home.html', {'name': 'Josh'})

def about(request):

    return render(request, 'about.html', {'name': 'Ya Slime'})

def add_info(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        return render(request, 'add.html')