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
        # Setup a single project
        project = Project.objects.create(
            name="Test Project",
            description="Project content")
        self.projects = Project.objects.all()

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

    def test_projects_GET(self):
        '''
        Test that projects view uses projects.html template
        '''
        client = Client()
        response = client.get(reverse('projects'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/projects.html')

    def test_single_project_GET(self):
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

    def test_add_project_GET(self):
        '''
        Test that add_project view uses add_project.html template
        '''
        response = self.client.get(reverse('add_project'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/add_project.html')

    def test_edit_project_GET(self):
        '''
        Test that edit_project view uses edit_project.html template
        '''
        response = self.client.get(reverse(
            'edit_project',
            args=[self.projects[0].id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/edit_project.html')

    def test_add_project_view_POST(self):
        '''
        Test that post requests to add_project view
        create a new project instance
        '''
        project = {
            'name': 'Test name',
            'description': 'Test content',
        }
        response = self.client.post(reverse('add_project'), project)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(Project.objects.count(), 2)
        self.assertEquals(self.projects[1].name, project['name'])

    def test_delete_project(self):
        '''
        Test that delete_project view deletes a project instance
        '''
        response = self.client.get(reverse(
            'delete_project',
            args=[self.projects[0].id]
        ))
        self.assertEqual(Project.objects.count(), 0)
        self.assertEquals(response.status_code, 302)
