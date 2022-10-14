from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    """
    A class to create a model form using the Testimonial model
    """
    class Meta:
        model = Testimonial
        fields = '__all__'
