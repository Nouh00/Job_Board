from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.companyDashboard, name='company-dashboard'),
    path('my-opportunites/', views.companyOpportunities, name='company-opportunities'),
    path('create-opportunity/', views.createOpportunity, name='create-opportunity'),
]