from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig

class TestTodoConfig(TestCase):
    def test_name_of_app(self):
        self.assertEqual(TodoConfig.name, 'todo')