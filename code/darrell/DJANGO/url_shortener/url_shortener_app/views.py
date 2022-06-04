from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UrlShortener
import uuid


def home(request):
    if request.method == 'GET':  # if its a GET request, just display the add.html template
        return render(request, 'pages/home.html')

    elif request.method == 'POST':  # if it's a POST request ..
        url = request.POST['url']
        code = str(uuid.uuid4())
        new_url = UrlShortener.objects.create(url=url, code=code)
        return render(request, 'pages/home.html', {'new_url': new_url})


# def saveurl(request):
    posted_url = UrlShortener.objects.get(id=id)
    # check the terminal, it should output the object before it gets deleted
    print(posted_url.url)
    return redirect('pages/saveurl.html')
