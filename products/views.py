from django.shortcuts import render
from .models import Product, Review
from .forms import ProductForm
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required


def view_templates(request):
    """
    A view to display all template products
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


@login_required
def add_review(request, product_id):
    """ A view to add a product review """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        rating = request.POST.get('rating', 1)
        content = request.POST.get('content', '')
        user = request.user
        review = Review.objects.create(
            product=product,
            rating=rating,
            content=content,
            created_by=user
        )

        if product.product_type == 'T':
            messages.success(request, 'Review successfully added!')
            return redirect(reverse(
                'template_product_detail', args=[product.id]))
        elif product.product_type == 'D':
            messages.success(request, 'Review successfully added!')
            return redirect(reverse(
                'design_product_detail', args=[product.id]))


@login_required
def delete_review(request, review_id):
    """ A view to delete a product review """
    review = get_object_or_404(Review, pk=review_id)
    user = request.user
    product = review.product

    # Admin user can delete all reviews.
    # Regular user can only review created by them.
    if user == review.created_by or user.is_superuser:
        review.delete()
        messages.success(request, 'Review successfully deleted!')
        return redirect(reverse(
                    'template_product_detail', args=[product.id]))
    else:
        if product.product_type == 'T':
            messages.error(request, 'You cannot delete this review!')
            return redirect(reverse(
                    'template_product_detail', args=[product.id]))
        elif product.product_type == 'D':
            messages.error(request, 'You cannot delete this review!')
            return redirect(reverse(
                    'design_product_detail', args=[product.id]))


def product_detail(request, product_id):
    """
    A view to display a single product
    """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)

    if product.product_type == 'T':
        title = 'Templates'
    else:
        title = 'Designs'

    context = {
        'product': product,
        'title': title,
        'reviews': reviews,
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
                return redirect(reverse(
                    'template_product_detail', args=[product.id]))
            elif product.product_type == 'D':
                return redirect(reverse(
                    'design_product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
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
                return redirect(reverse(
                    'template_product_detail',
                    args=[product.id]))
            elif product.product_type == 'D':
                return redirect(reverse(
                    'design_product_detail',
                    rgs=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(
            request,
            f'You are editing the following product: {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ A view to delete a store product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    if product.product_type == 'T':
        messages.success(request, 'Successfully deleted a template product!')
        return redirect(reverse('templates'))
    elif product.product_type == 'D':
        messages.success(request, 'Successfully deleted a design product!')
        return redirect(reverse('designs'))
