from django.shortcuts import render, redirect

from .models import TODO

def home(request):
    return render(request, 'home.html')

def todo_add(request):
    if request.method == 'GET':
        return render(request, 'add_todo.html')
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        TODO.objects.create(title = title, text = text, pub_date = pub_date)
        return redirect('add_list')

def index(request):
    return render(request, 'index.html',)

def todo_list(request):
    todolist = TODO.objects.all()
    return render(request, 'list.html', {'todolist': todolist})

def delete_list(request, id):
    todolist = TODO.objects.get(id=id)
    todolist.delete()
    return redirect('todo_list')
