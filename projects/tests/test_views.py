from django.test import TestCase, Client
from django.urls import reverse
from projects.models import Project
from django.contrib.auth import get_user_model
from projects.views import (
    projects,
    project,
    add_project,
    edit_project,
    delete_project)


class TestViews(TestCase):

    '''
    Unit testing for Project app views.
    '''

    def setUp(self):
        # Setup a single blog
        project = Project.objects.create(
            name="Test Project",
            description="Project content")
        self.projects = Project.objects.all()

    def test_projects_GET(self):
        '''
        Test that projects view uses projects.html template
        '''
        client = Client()
        response = client.get(reverse('projects'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/projects.html')

    def test_single_blog_GET(self):
        '''
        Test that project view uses project.html template
        '''
        client = Client()
        response = client.get(reverse(
            'project',
            args=[self.projects[0].id]),
            follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project.html')
