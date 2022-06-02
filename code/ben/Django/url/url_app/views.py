from django.shortcuts import render, redirect 
from url_app.models import URL_Short
from django.utils.crypto import get_random_string

def home(request):
    return render(request, 'pages/home.html')

def edit_url(request):
    url_list = URL_Short.objects.all() 
    context = {
       'url_list': url_list
        }
    return render(request, 'pages/edit_url.html', context)

def url(request):
    if request.method == 'GET': 
        return render(request, 'pages/url.html')
    elif request.method == 'POST': 
        url = request.POST['url']     
        char = get_random_string(length=5)
        url_short = 'https://' + char
        URL_Short.objects.create(url = url, url_short = url_short )
        return redirect('edit_url')