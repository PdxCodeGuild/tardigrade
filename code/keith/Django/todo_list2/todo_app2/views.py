
from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponse

# Create your views here.


def home(request):
    todos = Todo.objects.all() 
    return render(request, 'home.html', {"todos": todos})


def add_post(request):

        title = request.POST['new_todo']   # get the title from the POST submission, this comes from a form
        start_date = request.POST['date_made']     # get the text from the POST submission, this comes from a form
        end_date = request.POST['date_completed']
        completed = ""
        try:                     ### this says if theres an error in this first command then go to the lower one

            completed = request.POST.getlist('completed')[0]
        except:
            completed = False    #### using a boolean to deal with the check box i used for whether or not the todo was completed
                
        # add the new blog post to the database. objects.create() automatically saves the new blog post for us.
        Todo.objects.create(title = title, start_date = start_date, end_date = end_date, completed = completed )
        print(title, start_date, end_date, completed)  ## this prints those things in the terminal for me check
        return redirect('home')


def delete_todo(request, id):
    todo_item = Todo.objects.get(id=id) ##this queries the whole model 
    print(todo_item) ## check the terminal, it should output the object before it gets deleted
    todo_item.delete()
    return redirect('home')

def see_details(request, id): ##we get the id of the element. Remember, all elements are created with an ID in the database.
    print(id, "the ID")
    todo_item = Todo.objects.get(id = id) ## we are assigning the element to a variable
    print(todo_item, "the item in list")
    
    return render(request, 'details.html', {"todo_item": todo_item}) ## we are passing the context to the page
   

def update_post(request, id):
    blog_post = Todo.objects.get(id=id)
    blog_post.title = request.POST['title']
    blog_post.start_date = request.POST['start_date']
    blog_post.end_date = request.POST['end_date']
    blog_post.completed = ""

    try:                     ### this says if theres an error in this first command then go to the lower one

            blog_post.completed = request.POST.getlist('completed')[0]
    except:
            blog_post.completed = False    ##
    print(blog_post)
    blog_post.save()
    print(id)
    return redirect('home')