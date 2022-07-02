from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import Todo


def home(request): 
    todo_list = Todo.objects.all()
    return render(request, 'home.html', {"todo_list": todo_list})

def cross_off(request, id):
    todo_list = Todo.objects.get(id=id)
    todo_list.complete = True
    todo_list.save()
    return redirect('home')

def un_cross(request, id):
    todo_list = Todo.objects.get(id=id)
    todo_list.complete = False
    todo_list.save()
    return redirect('home')

def delete(request, id):
    todo_list = Todo.objects.get(id=id)
    todo_list.delete()
    return redirect('home')

def add(request):
    todo_list = Todo.objects.all()
    title = request.POST['add_item_to_list']
    Todo.objects.create(title=title)
    return redirect('home')

def completion_date(request, id):
    todo_list = Todo.objects.get(id=id)
    todo_list.completed_date = request.POST['select_date']
    todo_list.save()
    return redirect ('home')
