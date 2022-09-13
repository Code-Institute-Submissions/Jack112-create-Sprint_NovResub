from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required


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


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            if product.product_type == 'T':
                return redirect(reverse('template_product_detail', args=[product.id]))
            elif product.product_type == 'D':
                return redirect(reverse('design_product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ edit a store product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully updated a product!')
            if product.product_type == 'T':
                return redirect(reverse('template_product_detail', args=[product.id]))
            elif product.product_type == 'D':
                return redirect(reverse('design_product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing the following product: {product.name}')
        
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
