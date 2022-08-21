from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Product Admin Panel Setup
    """
    list_filter = ('project_type',)
    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
