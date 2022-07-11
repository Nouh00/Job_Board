from django.urls import path

from . import views


app_name = 'resume'


urlpatterns = [
    path('resume/<str:pk>/', views.resume, name='resume'),
    path('create-resume/', views.createResume, name='create-resume'),
    path('update-resume/<str:pk>/', views.updateResume, name='update-resume'),
    
    #education
    path('hx/<int:parent_id>/education/<int:id>/', views.education_update_hx_view, name='hx-education-detail'),
    path('hx/<int:parent_id>/education/', views.education_update_hx_view, name='hx-education-create'),
    path('hx/<int:parent_id>/education/<int:id>/delete/', views.education_delete_view, name='hx-education-delete'),
    
    #experience
    path('hx/<int:parent_id>/experience/<int:id>/', views.experience_update_hx_view, name='hx-experience-detail'),
    path('hx/<int:parent_id>/experience/', views.experience_update_hx_view, name='hx-experience-create'),
    path('hx/<int:parent_id>/experience/<int:id>/delete/', views.experience_delete_view, name='hx-experience-delete'),
    
    #work_experience
    path('hx/<int:parent_id>/work/<int:id>/', views.work_update_hx_view, name='hx-work-detail'),
    path('hx/<int:parent_id>/work/', views.work_update_hx_view, name='hx-work-create'),
    path('hx/<int:parent_id>/work/<int:id>/delete/', views.work_delete_view, name='hx-work-delete'),
    
    #publications
    path('hx/<int:parent_id>/publication/<int:id>/', views.publication_update_hx_view, name='hx-publication-detail'),
    path('hx/<int:parent_id>/publication/', views.publication_update_hx_view, name='hx-publication-create'),
    path('hx/<int:parent_id>/publication/<int:id>/delete/', views.publication_delete_view, name='hx-publication-delete'),
    
    #urlss
    path('hx/<int:parent_id>/url/<int:id>/', views.url_update_hx_view, name='hx-url-detail'),
    path('hx/<int:parent_id>/url/', views.url_update_hx_view, name='hx-url-create'),
    path('hx/<int:parent_id>/url/<int:id>/delete/', views.url_delete_view, name='hx-url-delete'),

    #skills
    path('hx/<int:parent_id>/skill/<int:id>/', views.skill_update_hx_view, name='hx-skill-detail'),
    path('hx/<int:parent_id>/skill/', views.skill_update_hx_view, name='hx-skill-create'),
    path('hx/<int:parent_id>/skill/<int:id>/delete/', views.skill_delete_view, name='hx-skill-delete'),
]
