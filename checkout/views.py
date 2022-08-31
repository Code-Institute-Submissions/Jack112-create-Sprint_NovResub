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

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, 'There are no items in your shopping bag!')
        return redirect('bag')
    
    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
