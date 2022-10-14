from django import forms
from .models import Product
from projects.models import Category


class ProductForm(forms.ModelForm):
    """
    Class to create a model form using Product model
    """

    class Meta:
        model = Product
        fields = '__all__'
