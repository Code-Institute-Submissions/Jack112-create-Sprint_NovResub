from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bag_contents
import stripe


def checkout(request):
    """
    A view to render the checkout page
    """

    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, 'There are no items in your shopping bag!')
        return redirect('bag')
    
    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100)

    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LO3O5DygYmPeIrevJYyv2d0reTyVqZAttBFpoyhWm5NKAS8Wa9BTchtwwOvyQM2dYZa8Na6HGxhfYUf2h1ujdjd00i2NtMVaj',
        'client_secret': 'test client secret',
    }

    return render(request, 'checkout/checkout.html', context)
