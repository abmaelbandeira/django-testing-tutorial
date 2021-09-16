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


    def test_project_list_view_retorna_status_correto(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)


    def test_project_list_view_renderiza_template_correto(self):
        response = self.client.get(self.list_url)
        self.assertTemplateUsed(response, 'budget/project-list.html')


    def test_project_create_view_retorna_status_correto(self):
        response = self.client.get(self.add_url)
        self.assertEquals(response.status_code, 200)


    def test_project_create_view_renderiza_template_correto(self):
        response = self.client.get(self.add_url)
        self.assertTemplateUsed(response, 'budget/add-project.html')


    def test_project_detail_view_retorna_status_correto_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)


    def test_project_detail_view_renderiza_template_correto_GET(self):
        response = self.client.get(self.detail_url)
        self.assertTemplateUsed(response, 'budget/project-detail.html')


    def teste_project_detail_POST_adds_new_expense(self):
        Category.objects.create(
            project=self.project1,
            name='development'
        )

        response = self.client.post(self.detail_url, {
            'title': 'expense1',
            'amount': 1000,
            'category': 'development'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.project1.expenses.first().title, 'expense1')


    def test_project_detail_POST_no_data(self):
        response = self.client.post(self.detail_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.project1.expenses.count(), 0)


    def test_project_detail_DELETE_deletes_expense(self):
        category1 = Category.objects.create(
            project=self.project1,
            name='development'
        )
        Expense.objects.create(
            project=self.project1,
            title='expense1',
            amount=1000,
            category=category1
        )

        response = self.client.delete(self.detail_url, json.dumps({
            'id': 1
        }))

        self.assertEquals(response.status_code, 204)
        self.assertEquals(self.project1.expenses.count(), 0)


    def test_project_detail_DELETE_no_id(self):
        category1 = Category.objects.create(
            project=self.project1,
            name='development'
        )
        Expense.objects.create(
            project=self.project1,
            title='expense1',
            amount=1000,
            category=category1
        )

        response = self.client.delete(self.detail_url)

        self.assertEquals(response.status_code, 404)
        self.assertEquals(self.project1.expenses.count(), 1)
