from rest_framework.serializers import ModelSerializer

from .models import Habit
from .validators import (HabitHaveJoyHabitOrReward, IsJoyHabitForJoyHabitField,
                         JoyHabitNotHaveJoyHabitOrReward,
                         PeriodInDaysNoMoreSeven)


class HabitSerializer(ModelSerializer):
    """Класс сериализатора модели привычки."""

    class Meta:
        model = Habit
        fields = ["place", "action", "is_joy", "notification_time"]
        validators = [JoyHabitNotHaveJoyHabitOrReward(),
                      HabitHaveJoyHabitOrReward(),
                      IsJoyHabitForJoyHabitField(),
                      PeriodInDaysNoMoreSeven()]
