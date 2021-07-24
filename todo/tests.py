import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Todo, CompletedTodoProxy


class TestTodoModel(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", password="sulavmhrzn")
        user = User.objects.first()
        Todo.objects.create(title="Todo 1", user=user)
        Todo.objects.create(title="Todo 2", is_completed=True, user=user)

    def test_todo_count(self):
        qs = Todo.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_todo_defaults_to_false(self):
        qs = CompletedTodoProxy.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_completed_todo_updates_date_completed(self):
        qs = CompletedTodoProxy.objects.first()
        self.assertIsNotNone(qs.date_completed)
        self.assertIsInstance(qs.date_completed, datetime.datetime)
