from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog


def home(request):
    if request.method == 'GET':
        return render(request, 'pages/home.html')
    elif request.method == "POST":
        title = request.POST['title']
        text = request.POST['text']
        temperature = [1, 2, 3, 4, 5]
        context = {
            "temperature": temperature,
            "text": text,
            "title": title
        }
        print(title, text)
        return render(request, 'pages/about.html', context)


def about(request):
    return render(request, 'pages/about.html')


def blog_posts(request):
    # gets all of the blog posts from the database and store them in a variable
    blogs = Blog.objects.all()

    # creates the context dictionary to send the blog posts to the template
    context = {
        'blogs': blogs
    }
    return render(request, 'pages/posts.html', context)


def add_post(request):
    if request.method == 'GET':  # if its a GET request, just display the add.html template
        return render(request, 'pages/add.html')
    elif request.method == 'POST':  # if it's a POST request ..
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        # add the new blog post to the database. objects.create() automatically saves the new blog post for us.
        Blog.objects.create(title=title, text=text, pub_date=pub_date)
        return redirect('posts')
