from rest_framework.validators import ValidationError


class JoyHabitNotHaveJoyHabitOrReward:

    def __call__(self, attrs):
        if attrs.get("is_joy"):
            if attrs.get("joy_habit") or attrs.get("reward"):
                raise ValidationError("У приятной привычки не может быть "
                                      "вознаграждения или другой связанной "
                                      "приятной привычки")


class HabitHaveJoyHabitOrReward:

    def __call__(self, attrs):
        if attrs.get("is_joy") is False:
            if attrs.get("joy_habit") and attrs.get("reward"):
                raise ValidationError("Должно быть заполнено либо поле приятной "
                                      "привычки, либо поле вознаграждения")


class IsJoyHabitForJoyHabitField:

    def __call__(self, attrs):
        if attrs.get("joy_habit"):
            if not attrs.get("joy_habit").is_joy:
                raise ValidationError("Связанной может быть только приятная привычка")


class PeriodInDaysNoMoreSeven:

    def __call__(self, attrs):
        if attrs.get("period_in_days") > 7:
            raise ValidationError("Периодичность повторения привычки не может быть более 7 дней")
        if attrs.get("period_in_days") < 1:
            raise ValidationError("Периодичность привычки не может быть меньше 1 дня")
