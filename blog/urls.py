from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<str:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<str:blog_id>/', views.delete_blog, name='delete_blog'),
    path('<str:blog_id>/', views.single_blog, name='single_blog'),
]
