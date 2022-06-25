from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_todo/', views.add_todo, name='add_todo'),
    # path('todo_view/', views.todo_view, name='todo_view')
    path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
    path('update_todo/<int:id>', views.update_todo, name='update_todo'),
    path('save_todo/<int:id>', views.save_todo, name='save_todo'),
]