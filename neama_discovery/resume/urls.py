from django.urls import path

from . import views


app_name = 'resume'


urlpatterns = [
    path('resume/<str:pk>/', views.resume, name='resume'),
    path('create-resume/', views.createResume, name='create-resume'),
    path('update-resume/<str:pk>/', views.updateResume, name='update-resume'),

    path('hx/<int:parent_id>/education/<int:id>/', views.education_update_hx_view, name='hx-education-detail'),
    path('hx/<int:parent_id>/education/', views.education_update_hx_view, name='hx-education-create'),

    path('hx/<int:parent_id>/experience/<int:id>/', views.experience_update_hx_view, name='hx-experience-detail'),
    path('hx/<int:parent_id>/experience/', views.experience_update_hx_view, name='hx-experience-create'),
    path('hx/<int:parent_id>/experience/<int:id>/delete/', views.experience_delete_view, name='hx-experience-delete'),

    # path('hx/<int:parent_id>/education/<int:id>/', views.education_update_hx_view, name='hx-education-detail'),
    # path('hx/<int:parent_id>/education/', views.education_update_hx_view, name='hx-education-create'),

    # path('hx/<int:parent_id>/education/<int:id>/', views.education_update_hx_view, name='hx-education-detail'),
    # path('hx/<int:parent_id>/education/', views.education_update_hx_view, name='hx-education-create'),

    # path('hx/<int:parent_id>/education/<int:id>/', views.education_update_hx_view, name='hx-education-detail'),
    # path('hx/<int:parent_id>/education/', views.education_update_hx_view, name='hx-education-create'),
]
