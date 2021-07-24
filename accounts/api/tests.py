from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status


class TestUserRegister(APITestCase):
    def setUp(self):
        User.objects.create(username="test", password="sulavmhrzn")
        self.url = reverse("signup")

    def test_user_register(self):
        data = {
            "username": "testuser",
            "password": "sulavmhrzn",
            "password2": "sulavmhrzn",
        }

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.data["username"], data["username"])
        self.assertFalse("password" in response.data)

    def test_user_register_checks_fields(self):
        data = {
            "username": "testuser",
            "password": "sulavmhrzn",
            "password2": "sulavmhrzns",
        }

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
