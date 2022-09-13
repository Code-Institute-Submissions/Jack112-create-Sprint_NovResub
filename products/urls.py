from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.view_templates, name='templates'),
    path('designs/', views.view_designs, name='designs'),
    path('templates/<str:product_id>/', views.product_detail, name='template_product_detail'),
    path('designs/<str:product_id>/', views.product_detail, name='design_product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<str:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<str:product_id>/', views.delete_product, name='delete_product'),
]
