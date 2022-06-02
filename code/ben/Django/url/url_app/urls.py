from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('url', views.url, name = 'url'),
    path('edit_url', views.edit_url, name = 'edit_url')
]