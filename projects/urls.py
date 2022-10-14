from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add_project, name='add_project'),
    path(
        'delete/<str:project_id>/',
        views.delete_project,
        name='delete_project'),
    path('edit/<str:project_id>/', views.edit_project, name='edit_project'),
    path('<str:project_id>/', views.project, name='project'),
]
