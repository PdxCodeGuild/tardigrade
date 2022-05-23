from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name = 'home'),
    path('add_todo/', views.todo_add, name = 'add_list' ),
    path('list_todo/', views.todo_list, name = 'todo_list' ),
    path('del_todo/<int:id>', views.delete_list, name = 'delete_list' ),

]