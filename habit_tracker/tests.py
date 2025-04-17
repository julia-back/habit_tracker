from django.shortcuts import reverse
from rest_framework.test import APITestCase

from habit_tracker.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test1@test.com", username="test1", password="1234")
        self.joy_habit = Habit.objects.create(user=self.user, place="Кафе у дома", action="Заказать десерт",
                                              is_joy=True, notification_time="17:00:00")
        self.habit = Habit.objects.create(user=self.user, place="Парк", action="Сходить на пробежку",
                                          is_joy=False, notification_time="16:00:00", joy_habit=self.joy_habit)

    def test_habit_create(self):
        url = reverse("habit_tracker:habit_create")
        habit_data = {"place": "Дом", "action": "Сделать зарядку",
                      "is_joy": False, "notification_time": "7:00:00"}
        response = self.client.post(url, habit_data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user)
        response = self.client.post(url, habit_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get("action"), "Сделать зарядку")

    def test_habit_list(self):
        url = reverse("habit_tracker:habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("count"), 2)

    def test_habit_list_public(self):
        url = reverse("habit_tracker:habit_public_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("count"), 0)

    def test_habit_retrieve(self):
        url = reverse("habit_tracker:habit_retrieve", args=[self.habit.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("action"), "Сходить на пробежку")

    def test_habit_update(self):
        url = reverse("habit_tracker:habit_update", args=[self.habit.id])
        data = {"notification_time": "20:00:00"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("action"), "Сходить на пробежку")
        self.assertEqual(response.json().get("notification_time"), "20:00:00")

    def test_habit_delete(self):
        url = reverse("habit_tracker:habit_delete", args=[self.habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)

        self.client.force_authenticate(self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
