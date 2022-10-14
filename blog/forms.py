from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    """
    Create new form from Blog model
    """

    class Meta:
        model = Blog
        fields = '__all__'
