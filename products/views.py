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


def product_detail(request, product_id):
    """
    A view to display a single product
    """

    product = get_object_or_404(Product, pk=product_id)

    print(product.product_type)

    if product.product_type == 'T':
        title = 'Templates'
    else:
        title = 'Designs'

    context = {
        'product': product,
        'title': title,
    }

    return render(request, 'products/product_detail.html', context)
