from django.shortcuts import reverse
from rest_framework.test import APITestCase

from .models import User


class UserAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test1@test.com", username="test1", password="1234")

    def test_token_obtain_pair(self):
        url = reverse("users:token_obtain_pair")
        data = {"email": "test1@test.com", "username": "test1", "password": "1234"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get("refresh"))
        self.assertTrue(response.json().get("access"))

    def test_user_register(self):
        url = reverse("users:user_register")
        data = {"email": "test2@test.com", "username": "test2", "password": "1234"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get("email"), "test2@test.com")
        self.assertEqual(response.json().get("username"), "test2")

    def test_user_retrieve(self):
        url = reverse("users:user_retrieve", args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("email"), "test1@test.com")

    def test_user_update(self):
        url = reverse("users:user_update", args=[self.user.pk])
        data = {"username": "other_test1"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("email"), "test1@test.com")
        self.assertEqual(response.json().get("username"), "other_test1")

    def test_user_delete(self):
        url = reverse("users:user_delete", args=[self.user.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
