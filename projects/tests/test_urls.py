from django.test import TestCase
from django.urls import reverse, resolve
from projects.views import projects, project, add_project, edit_project, delete_project


class TestUrls(TestCase):

    '''
    Unit testing for Project app urls
    '''

    def test_projects_url_resolves(self):
        '''
        Test that projects url uses projects view.
        '''
        url = reverse('projects')
        self.assertEquals(projects, resolve(url).func)

    def test_project_url(self):
        '''
        Test that project url uses project view.
        '''
        url = reverse('project', args=[1])
        self.assertEquals(project, resolve(url).func)

    def test_add_project_url(self):
        '''
        Test that add_project url uses add_project view.
        '''
        url = reverse('add_project')
        self.assertEquals(add_project, resolve(url).func)

    def test_edit_project_url(self):
        '''
        Test that edit_project url uses edit_project view.
        '''
        url = reverse('edit_project', args=[1])
        self.assertEquals(edit_project, resolve(url).func)

    def test_delete_project_url(self):
        '''
        Test that delete_project url uses delete_project view.
        '''
        url = reverse('delete_project', args=[1])
        self.assertEquals(delete_project, resolve(url).func)
