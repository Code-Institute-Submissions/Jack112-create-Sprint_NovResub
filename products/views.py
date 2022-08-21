from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404


def view_templates(request):
    """
    Display all products
    """

    products = Product.objects.filter(product_type="T")

    context = {
        'products': products
    }

    return render(request, 'products/templates.html', context)


def view_designs(request):
    """
    A view to display all design products
    """

    products = Product.objects.filter(product_type="D")

    context = {
        'products': products
    }

    return render(request, 'products/designs.html', context)
