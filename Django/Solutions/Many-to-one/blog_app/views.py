from tkinter import E
from django.shortcuts import render,redirect
from .models import Reporter, Article

## https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/

def add_reporter(request):
    if request.method=="GET":
        return render(request, 'home.html')
    elif request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        Reporter.objects.create(first_name=first_name, last_name=last_name, email=email)
        return redirect('add_reporter')

def add_article(request):
    if request.method == 'GET':
        reporters = Reporter.objects.all()
        return render(request, 'articles.html', {"reporters":reporters})
    elif request.method == "POST":
        headline = request.POST['headline']
        pub_date= request.POST['pub_date']
        reporter = Reporter.objects.get(id=request.POST['reporter']) ##Queries the database and saves an instance of the reporter object in the variable reporter
        Article.objects.create(headline=headline, pub_date=pub_date, reporter=reporter)
        print(reporter,pub_date,headline)
        return redirect('add_article')
 

def view_all(request):
    #Article.objects.filter(reporter__pk=1) ##pk is primary key. This gives a list of articles linke to the reporter with ID of 1
    #Reporter.objects.filter(article__pk=1) Gives a list of reporters linked to an article
    all_reporters = Reporter.objects.all()   
    return render(request, 'list.html', {"all_reporters":all_reporters})