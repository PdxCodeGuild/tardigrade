from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('cross_off/<int:id>', views.cross_off, name='cross_off'),
path('un_cross/<int:id>', views.un_cross, name='un_cross'),
path('delete/<int:id>', views.delete, name='delete'),
path('add', views.add, name='add'),
path('completion_date/<int:id>', views.completion_date, name='completion_date')
]