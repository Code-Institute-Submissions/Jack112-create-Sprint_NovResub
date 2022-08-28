from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """
    A view to render the checkout page
    """

    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, 'There are no items in your shopping bag!')
        return redirect('bag')
    
    order_form = OrderForm()

    context = {
        'order_form': order_form
    }

    return render(request, 'checkout/checkout.html', context)
