from django.contrib import admin
from .models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    """
    Product Admin Panel Setup
    """
    list_filter = ('product_type',)
    ordering = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    """
    Review Admin Panel Setup
    """
    fields = ('product', 'rating', 'content', 'created_by', 'created_at')
    list_display = ('product', 'rating', 'content', 'created_by', 'created_at')
    readonly_fields = (
        'rating',
        'content',
        'created_by',
        'product',
        'created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
