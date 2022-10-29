from django.test import TestCase
from django.urls import reverse, resolve
from home.views import home


class TestUrls(TestCase):

    '''
    Unit testing for Home app urls
    '''

    def test_home_url_resolves(self):
        '''
        Test that home url uses home view.
        '''
        url = reverse('home')
        self.assertEquals(home, resolve(url).func)
