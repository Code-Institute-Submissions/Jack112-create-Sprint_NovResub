from django.shortcuts import render
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def testimonials(request):
    """
    A view to render all testimonials for admin users.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


def add_testimonial(request):
    """
    View to add new testimonial
    """

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial successfully added')
            return redirect('home')
        else:
            messages.error(
                request,
                """Unable to add a new testimonial at this time.
                Please try again later""")

    form = TestimonialForm()

    context = {
        'form': form
    }

    return render(request, 'testimonials/add_testimonial.html', context)


@login_required
def delete_testimonial(request, testimonial_id):
    """
    A view to delete a testimonial.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    testimonial.delete()
    messages.success(request, 'Testimonial successfully deleted.')
    return redirect('testimonials')
