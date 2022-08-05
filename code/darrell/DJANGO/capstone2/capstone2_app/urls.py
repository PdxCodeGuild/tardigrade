from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('claims/', views.claims, name='claims'),
    path('email/', views.email, name='email'),
    path('add_claims/', views.add_claims, name='add_claims'),
    path('', views.splash, name='splash'),
    path('email_details/<int:id>', views.email_details, name = 'email_details'),
    path('claim_details/<int:id>', views.claim_details, name = 'claim_details'),
    path('update_claim/<int:id>', views.update_claim, name = 'update_claim'),
    path('delete_claim/<int:id>', views.delete_claim, name = 'delete_claim'),
    path('api/claims/', views.claims_api),
    path('chart/', views.chart, name='chart'),
    path('search/', views.search, name = 'search')
]
