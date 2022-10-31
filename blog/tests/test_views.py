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

        # User setup and login
        username = 'Test'
        email = 'test@test.com'
        password = 'testpassword1234'
        first_name = 'testUserFirst'
        last_name = 'testUserLast'
        user_model = get_user_model()
        self.user = user_model.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name)

        # Login test user
        login = self.client.login(email=email, password=password)
        self.assertTrue(login)

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

    def test_add_blog_GET(self):
        '''
        Test that add_blog view uses add_blog.html template
        '''
        response = self.client.get(reverse('add_blog'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_blog.html')

    def test_add_blog_view_POST(self):
        '''
        Test that post requests to add_blog view create a new blog instance
        '''
        blog = {
            'title': 'Test title',
            'name': 'Test name',
            'content': 'Test content',
        }
        response = self.client.post(reverse('add_blog'), blog)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(Blog.objects.count(), 2)
        self.assertEquals(self.blogs[1].title, blog['title'])

    def test_edit_blog_GET(self):
        '''
        Test that edit_blog view uses edit_blog.html template
        '''
        response = self.client.get(reverse(
            'edit_blog',
            args=[self.blogs[0].id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_blog.html')

    def test_edit_blog_POST(self):
        '''
        Test that post requests to edit_blog view updates blog instance
        '''
        blog = self.blogs.get(title='Test Blog')
        response = self.client.post(reverse(
            'edit_blog',
            kwargs={'blog_id': blog.id}),
            {'title': 'Updated blog title'},
            )
        self.assertEqual(response.status_code, 200)
        blog.refresh_from_db()
        self.assertEqual(blog.title, 'Updated blog title')

    def test_delete_blog(self):
        '''
        Test that delete_blog view deletes a blog instance
        '''
        response = self.client.get(reverse(
            'delete_blog',
            args=[self.blogs[0].id]
        ))
        self.assertEqual(Blog.objects.count(), 0)
        self.assertEquals(response.status_code, 302)
