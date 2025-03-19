from django.core.validators import MaxValueValidator
from django.db import models
from users.models import User
from datetime import time


class Habit(models.Model):
    """
    Модель привычки, связана с моделью пользователя. В зависимости от поля is_joy
    может быть полезной (is_joy = False) и будет иметь возможность заполнения полей
    joy_habit (связаная приятная привычка) и reward (вознаграждение на выполнение привычки)
    или может быть приятной (is_joy = True). В зависимости от значения поля is_public
    может быть публичной и доступной для просмотра другими пользователями.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=50)
    process_time = models.TimeField(blank=True, null=True, validators=[MaxValueValidator(time(minute=2))])
    action = models.TextField(max_length=1000)
    joy_habit = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
    reward = models.CharField(max_length=250, blank=True, null=True)
    is_joy = models.BooleanField()
    period_in_days = models.IntegerField(default=1)
    notification_time = models.TimeField()
    is_public = models.BooleanField(default=False)
