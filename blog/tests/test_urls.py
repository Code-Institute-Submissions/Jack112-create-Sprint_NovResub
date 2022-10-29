from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import blog, single_blog, add_blog, edit_blog, delete_blog


class TestUrls(TestCase):

    '''
    Unit testing for Blog app urls
    '''

    def test_blogs_url_resolves(self):
        '''
        Test that blog url uses blogs view.
        '''
        url = reverse('blog')
        self.assertEquals(blog, resolve(url).func)

    def test_single_blog_url(self):
        '''
        Test that single_blog url uses single_blog view.
        '''
        url = reverse('single_blog', args=[1])
        self.assertEquals(single_blog, resolve(url).func)

    def test_add_blog_url(self):
        '''
        Test that add_blog url uses add_blog view.
        '''
        url = reverse('add_blog')
        self.assertEquals(add_blog, resolve(url).func)

    def test_edit_blog_url(self):
        '''
        Test that edit_blog url uses edit_blog view.
        '''
        url = reverse('edit_blog', args=[1])
        self.assertEquals(edit_blog, resolve(url).func)

    def test_delete_blog_url(self):
        '''
        Test that blog url uses blogs view.
        '''
        url = reverse('delete_blog', args=[1])
        self.assertEquals(delete_blog, resolve(url).func)
