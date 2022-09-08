from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm

def profile(request):
    """
    A view to render the users profile
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()
    form = UserProfileForm(instance=profile)

    context = {
        'profile': profile,
        'orders': orders,
        'form': form,
    }

    return render(request, 'profiles/profile.html', context)

