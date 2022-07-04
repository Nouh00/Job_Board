from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('recruiter-profile/<str:pk>/', views.recruiterProfile, name="recruiter-profile"),
    path('update-recruiter/<str:pk>/', views.updateRecruiter, name="update-recruiter"),
]

'''
    
    path('register/', views.registerPage, name='register'),

    path('volunteer-profile/<str:pk>/', views.volProfile, name="vol-profile"),
    path('update-volprofile/', views.updateProfileVol, name='update-volprofile'),'''