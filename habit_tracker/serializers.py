from rest_framework.serializers import ModelSerializer
from .models import Habit
from .validators import (IsJoyHabitForJoyHabitField, JoyHabitNotHaveJoyHabitOrReward,
                         HabitHaveJoyHabitOrReward, PeriodInDaysNoMoreSeven)


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        exclude = ["user"]
        validators = [JoyHabitNotHaveJoyHabitOrReward(),
                      HabitHaveJoyHabitOrReward(),
                      IsJoyHabitForJoyHabitField(),
                      PeriodInDaysNoMoreSeven()]
