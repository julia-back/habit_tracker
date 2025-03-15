from django.core.validators import MaxValueValidator
from django.db import models
from users.models import User
from datetime import time


class Habit(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=50, blank=True, null=True)
    time_to_complete = models.TimeField(blank=True, null=True, validators=[MaxValueValidator(time(minute=2))])
    action = models.TextField(max_length=1000, blank=True, null=True)
    joy_habit = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
    reward = models.CharField(max_length=250, blank=True, null=True)
    is_joy = models.BooleanField()
    period_in_days = models.IntegerField(default=1)
    notification_time = models.TimeField()
    is_public = models.BooleanField(default=False)
