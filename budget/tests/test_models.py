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
