from turtle import title
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def todo(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        title= request.POST['title']
        text= request.POST['text']
        pub_date= request.POST['pub_date'] 
        print(title, text, pub_date)
        return redirect('add')

