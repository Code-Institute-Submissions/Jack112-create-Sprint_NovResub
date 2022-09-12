from django import forms
from .models import Product
from projects.models import Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

