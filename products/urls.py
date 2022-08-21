from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.view_templates, name='templates'),
    path('designs/', views.view_designs, name='designs'),
    path('templates/<str:product_id>/', views.product_detail, name='product_detail'),
    path('designs/<str:product_id>/', views.product_detail, name='product_detail'),
]
