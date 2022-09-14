from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib import messages
from checkout.models import Order
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    """
    A view to render the users profile
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    context = {
        'profile': profile,
        'orders': orders,
        'form': form,
    }

    return render(request, 'profiles/profile.html', context)

