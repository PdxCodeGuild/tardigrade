from tkinter import E
from django.shortcuts import render,redirect
from .models import Reporter, Article

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
        reporter = Reporter.objects.get(id=request.POST['reporter'])
        Article.objects.create(headline=headline, pub_date=pub_date, reporter=reporter)
        # Article.objects.create(headline="This is a test", pub_date=date(2005, 7, 27), reporter=r3)
        print(reporter,pub_date,headline)
        return redirect('add_article')
 

def view_all(request):
    #Article.objects.filter(reporter__pk=1) ##pk is primary key
    #Reporter.objects.filter(article__pk=1)
    all_reporters = Reporter.objects.all()
    all_articles = Article.objects.all()
    context = {
        "all_reporters": all_reporters,
        "all_articles":all_articles
    }
    return render(request, 'list.html', context)