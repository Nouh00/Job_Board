from django.urls import path

from . import views

urlpatterns = [
    path('opportunities/', views.opportunities, name='opportunities'),
    path('opportunity/<str:pk>/', views.singlOpportunity, name='single-opportunity'),
    path('add-opportunity/', views.addOpportunity, name='add-opportunity'),
    path('apply-opportunity/<str:pk>/', views.applyOpportunity, name='apply-opportunity'),
]