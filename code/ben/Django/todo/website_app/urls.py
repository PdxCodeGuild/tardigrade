from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('posts/', views.posts, name = 'posts'),
    path('todo/', views.to_do, name = 'todo'),
    path('todo_details/<int:id>', views.todo_details, name='todo_details'),
    path('update_todo/<int:id>', views.update_todo, name='update_todo'),
    path('remove/<int:id>', views.remove, name='remove')
]