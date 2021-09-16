from django.test import SimpleTestCase
from budget.forms import ExpenseForm


class TestForms(SimpleTestCase):

    def test_expense_form_valid_data(self):
        form = ExpenseForm(data={
            'title': 'expense1',
            'amount': 2000,
            'category': 'development'
        })
        self.assertTrue(form.is_valid())