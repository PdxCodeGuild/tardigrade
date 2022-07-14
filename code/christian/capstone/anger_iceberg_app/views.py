from django.http import HttpResponse
from django.shortcuts import render, redirect
# Import the below to run an API. Heads up, you have to import rquests in the terminal:
# pip install requests
from . models import Quote
import requests



### DONT FORGET - You'll need to eventually import your class name

# Create your views here.

def home(request):
    return render(request, "home.html")

def iceberg(request):
    response = requests.get("https://type.fit/api/quotes")
    data = response.json()

    print(data[0:9]) ###TEST STATEMENT - This is only a partial list for time/readibility
    for saying in data:
        try:
            author = saying["author"]
            if author == None:
                author = "Anonymous"
            Quote.objects.create(text=saying["text"], author=author)
        except:
            continue
    all_quotes = Quote.objects.all()
    return render(request, "anger_iceberg.html", {"all_quotes": all_quotes})



    