from django.test import TestCase, Client
from django.urls import reverse
from budget.models import Project, Category, Expense
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_list_view_retorna_status_correto(self):
        response = self.client.get(reverse('list'))
        self.assertEquals(response.status_code, 200)

    def test_list_view_renderiza_template_correto(self):
        response = self.client.get(reverse('list'))
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_create_view_retorna_status_correto(self):
        response = self.client.get(reverse('add'))
        self.assertEquals(response.status_code, 200)

    def test_create_view_renderiza_template_correto(self):
        response = self.client.get(reverse('add'))
        self.assertTemplateUsed(response, 'budget/add-project.html')
