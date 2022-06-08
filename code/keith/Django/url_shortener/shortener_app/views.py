from django.shortcuts import render,redirect  ### allows me to both render and redirect :)
import random ### lets me import random numbers 
from .models import shortenURL  ### brings in my model to use
import string

# Create your views here.
def index(request):
    return render(request,'index.html')
 
def createshorturl(request):
    if request.method == 'POST':
        
            shortened_url = ''.join(random.choice(string.ascii_letters)  ### gets my random numbers and makes them into a string
                           for x in range(5)) ### gives me a 5 character shortened URL
            original_url = request.POST["url"]
            new_url = shortenURL(original_url=original_url, shortened_url=shortened_url)
            new_url.save()
         
           
            return redirect('/')
  
def urlcreated(request):   #### this is the view to displays my list of submitted urls to shorten
    url=shortenURL.objects.all()  #### this goes through my model and displays it as a table
    return render(request,'urls.html',{'url':url})  ### this is rendering my actual html view 