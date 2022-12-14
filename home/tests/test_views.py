from django.test import TestCase, Client
from django.urls import reverse
from home.views import home


class TestViews(TestCase):

    '''
    Unit testing for Home app views.
    '''

    def test_home_GET(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
