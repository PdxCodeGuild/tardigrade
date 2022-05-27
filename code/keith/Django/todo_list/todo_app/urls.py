from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),   ### this just connects my home page
    path('add/', views.add_post, name = 'add_posts'),    ### this is a route connecting my add page
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'), ### this is a route connecting my delete pathway
    path('details/<int:id>', views.see_details, name = 'see_details'),
    path('update_post/<int:id>', views.update_post, name = 'update_post')
    
]