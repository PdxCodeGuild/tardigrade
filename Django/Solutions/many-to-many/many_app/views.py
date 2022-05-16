from django.shortcuts import render, HttpResponse
from . models import *
#https://stackoverflow.com/questions/44433834/how-do-i-iterate-through-a-manytomanyfield-in-django-jinja-project
# Create your views here.
def home(request):
    all_pubs = Publication.objects.all()
    articles_in_pubs = Publication.objects.get(id=2).article_set.all()
    ## I give you an article, find all publications:
    pubs_linked_to_articles = Article.objects.get(id=2).publications.all()
    print(pubs_linked_to_articles)
    return HttpResponse('egerg')