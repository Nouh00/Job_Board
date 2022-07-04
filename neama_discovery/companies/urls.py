from django.urls import path

from . import views

urlpatterns = [
    path('companies/', views.companies, name='companies'),
    path('company/<str:pk>/', views.singlCompany, name='single-company'),
    path('add-company/', views.addCompany, name='add-company')
]