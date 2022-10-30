from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Blog
from django.contrib.auth import get_user_model
from blog.views import blog, single_blog, add_blog, edit_blog, delete_blog


class TestViews(TestCase):

    '''
    Unit testing for Blog app views.
    '''

    def setUp(self):
        # Setup a single blog
        blog = Blog.objects.create(title="Test Blog", name="Jack")
        self.blogs = Blog.objects.all()

    def test_blogs_GET(self):
        '''
        Test that blog view uses blogs.html template
        '''
        client = Client()
        response = client.get(reverse('blog'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogs.html')

    def test_single_blog_GET(self):
        '''
        Test that single_blog view uses single_blog.html template
        '''
        client = Client()
        response = client.get(reverse(
            'single_blog',
            args=[self.blogs[0].id]),
            follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/single_blog.html')
