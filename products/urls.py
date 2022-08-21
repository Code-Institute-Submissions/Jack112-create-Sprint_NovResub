from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.view_templates, name='templates'),
    path('designs/', views.view_designs, name='designs'),
]
