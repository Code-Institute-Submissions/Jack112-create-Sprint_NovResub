from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Blog
from blog.views import blog, single_blog, add_blog, edit_blog, delete_blog


class TestViews(TestCase):

    '''
    Unit testing for Blog app views.
    '''

    def test_blogs_GET(self):
        '''
        Test that blog view uses blogs.html template
        '''
        client = Client()
        response = client.get(reverse('blog'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogs.html')
