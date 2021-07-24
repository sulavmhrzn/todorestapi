from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from todo.models import Todo


class TestTodoViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create(username="testuser", password="sulavmhrzn")
        self.client.force_authenticate(user=user)

    def _post_todo(self):
        """Helper method to post to a database"""
        data = {"title": "Test 1"}
        url = reverse("todo-list")
        return self.client.post(url, data=data)

    def test_not_logged_in_user_cant_view(self):
        url = reverse("todo-list")
        self.client.logout()
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_view(self):
        url = reverse("todo-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_post(self):
        response = self._post_todo()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)

    def test_logged_in_user_can_update(self):
        self._post_todo()

        url = reverse("todo-detail", args="1")
        response = self.client.patch(url, data={"title": "Test Update"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_is_completed_updates_date_completed(self):
        self._post_todo()

        url = reverse("todo-detail", args="1")
        response = self.client.patch(url, data={"is_completed": "True"})
        self.assertIsNotNone(response.data.get("date_completed"))

    def test_logged_in_users_can_delete(self):
        self._post_todo()

        url = reverse("todo-detail", args="1")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
