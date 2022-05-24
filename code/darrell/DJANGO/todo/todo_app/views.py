from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoItem


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def todo_items(request):
    # gets all of the blog posts from the database and store them in a variable
    todos = TodoItem.objects.all()

    # creates the context dictionary to send the blog posts to the template
    context = {
        'todos': todos
    }
    return render(request, 'pages/todo_items.html', context)


def add_todo_item(request):
    if request.method == 'GET':  # if its a GET request, just display the add.html template
        return render(request, 'pages/add.html')
    elif request.method == 'POST':  # if it's a POST request ..
        description = request.POST['description']
        created_date = request.POST['created_date']
        completed_date = request.POST['completed_date']
        is_completed = request.POST['is_completed']

        # add the new todo item to the database. objects.create() automatically saves the new todo item for us.
        TodoItem.objects.create(description=description, created_date=created_date,
                                completed_date=completed_date, is_completed=is_completed)
        return redirect('todo_items')


def delete_item(request, id):
    todo_item = TodoItem.objects.get(id=id)
    # check the terminal, it should output the object before it gets deleted
    print(todo_items)
    todo_item.delete()
    return redirect('todo_items')


# we get the id of the element. Remember, all elements are created with an ID in the database.
def see_details(request, id):
    # we are assigning the element to a variable
    item = TodoItem.objects.get(id=id)
    # we are passing the context to the page
    return render(request, 'pages/details.html', {"item": item})


def update_item(request, id):
    todo_item = TodoItem.objects.get(id=id)
    todo_item.description = request.POST['description']
    todo_item.created_date = request.POST['created_date']
    todo_item.completed_date = request.POST['completed_date']
    todo_item.is_completed = request.POST['is_completed']
    print(todo_item)
    todo_item.save()
    return redirect('todo_items')


def search_items(request):
    search = request.POST['search_item']
    todo_item = TodoItem.objects.filter(description__startswith=search)
    print(search, todo_item)
    return render(request, 'pages/home.html', {"todo_item": todo_item})
