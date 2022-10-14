from django.shortcuts import render
from testimonials.models import Testimonial


def home(request):
    """
    A view to return the home page
    """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'home/index.html', context)
