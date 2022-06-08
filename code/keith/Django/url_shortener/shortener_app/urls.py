from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),  ### returns my home page of sorts "/"
    path('createshorturl',views.createshorturl,name="createshorturl"),  ### abstract URL thats really a function
    path("urlcreated",views.urlcreated,name="urlcreated"),   #### this is linking my actual second view
]