from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('anger-iceberg/', views.iceberg, name='anger-iceberg'),
]
