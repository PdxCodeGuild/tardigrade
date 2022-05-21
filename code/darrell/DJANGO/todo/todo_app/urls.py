from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('todo_items/', views.todo_items, name='todo_items'),
    path('add/', views.add_todo_item, name='add_todo_items'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),
    path('details/<int:id>', views.see_details, name='see_details'),
    path('update_item/<int:id>', views.update_item, name='update_item')
]
