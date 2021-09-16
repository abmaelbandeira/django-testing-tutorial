from django.test import TestCase
from budget.models import Project, Category, Expense


class TestModels(TestCase):

    def setUp(self):
        self.project1 = Project.objects.create(
            name='Project 1',
            budget=10000
        )

    def test_project_atribui_slug_no_create(self):
        self.assertEquals(self.project1.slug, 'project-1')

    def test_project_budget_left(self):
        category1 = Category.objects.create(
            project=self.project1,
            name='development'
        )
        Expense.objects.create(
            project=self.project1,
            title='Teste1',
            amount=2000,
            category=category1
        )
        Expense.objects.create(
            project=self.project1,
            title='Teste2',
            amount=1000,
            category=category1
        )

        self.assertEquals(self.project1.budget_left, 7000)