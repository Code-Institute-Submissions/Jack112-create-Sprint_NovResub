from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    """
    A class to create a model form using the Project model
    """
    class Meta:
        model = Project
        fields = '__all__'
