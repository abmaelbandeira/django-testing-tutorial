from django.test import TestCase, Client
from django.urls import reverse
from budget.models import Project, Category, Expense
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.add_url = reverse('add')
        self.detail_url = reverse('detail', args=['project1'])

        self.project1 = Project.objects.create(
            name='project1',
            budget=10000
        )

    def test_list_view_retorna_status_correto(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_list_view_renderiza_template_correto(self):
        response = self.client.get(self.list_url)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_create_view_retorna_status_correto(self):
        response = self.client.get(self.add_url)
        self.assertEquals(response.status_code, 200)

    def test_create_view_renderiza_template_correto(self):
        response = self.client.get(self.add_url)
        self.assertTemplateUsed(response, 'budget/add-project.html')

    def test_detail_view_retorna_status_correto(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
