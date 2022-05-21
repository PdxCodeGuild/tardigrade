from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo 

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')


def posts(request):
    return render(request, 'pages/posts.html')

def posts(request):
    todos = todo.objects.all() 
  
    context = {
       'todos': todos
    }
    return render(request, 'pages/posts.html', context)

def to_do(request):
    if request.method == 'GET': 
        return render(request, 'pages/todo.html')
    elif request.method == 'POST': 
        title = request.POST['title']  
        create_date  = request.POST['create_date'] 
        completed_date  = request.POST['completed_date'] 
        text = request.POST['text']     
        if (request.POST['complete'] == 'False'):
            complete = False
        else:
            complete = True
        todo.objects.create(title = title, text = text, create_date = create_date, complete = complete, completed_date = completed_date)
        return redirect ('posts')

def todo_details(request, id):
    todo_post = todo.objects.get(id=id)
    return render(request, 'pages/edit.html', {"todo_post": todo_post})

def update_todo(request, id):
    todo_post = todo.objects.get(id=id)
    todo_post.title = request.POST['title'] 
    todo_post.create_date = request.POST['create_date']  
    todo_post.completed_date = request.POST['ompleted_date'] 
    todo_post.text = request.POST['text']
    todo_post.complete = request.POST['complete']
    todo_post.save()
    return redirect('posts')

def remove(request, id):
    todo_post = todo.objects.get(id=id)
    todo_post.delete()
    return redirect('posts')
