from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem

# Create your views here.
# def home(request):
#     # return HttpResponse('This is the home page')
#     return render(request, 'home.html')

def add_todo(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        description = request.POST['description']
        start_date = request.POST['start_date']
        complete_date = request.POST['complete_date']
        completed = False
        print(description, start_date, complete_date, completed)
        TodoItem.objects.create(description=description, start_date=start_date, complete_date=complete_date, completed=completed)
        return redirect('home')

def home(request):
    todo_items = TodoItem.objects.all()
    print("all tasks:", todo_items)
    return render(request, 'home.html', {'todo_items': todo_items})

def delete_todo(request, id):
    todo_item = TodoItem.objects.get(id=id)
    todo_item.delete()
    return redirect('home')

def update_todo(request, id):
    todo_item = TodoItem.objects.get(id=id)
    return render(request, 'update_todo.html', {'todo_item': todo_item})

def save_todo(request, id):
    task = TodoItem.objects.get(id=id)
    task.description = request.POST['description']
    task.start_date = request.POST['start_date']
    task.complete_date = request.POST['complete_date']
    task.completed = ''
    try:
        task.completed = request.POST['completed'] #[]
        print("LOOK HERE", request.POST['completed'])
    except:
        task.completed = False 
    if task.completed =='on':
        task.completed = True
        print("TASK STATUS", task.completed)  
    task.save()
    return redirect("home")

