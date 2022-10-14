from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    A class to create a model form using the UserProfile model
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add custom labels to user profile form
        """
        super().__init__(*args, **kwargs)
        labels = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
            'default_country': 'Country',
        }

        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].label = f'{labels[field]} *'
            else:
                self.fields[field].label = labels[field]
