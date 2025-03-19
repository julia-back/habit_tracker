from rest_framework.validators import ValidationError


class JoyHabitNotHaveJoyHabitOrReward:
    """Класс валидатора. Проверяет, что приятная привычка не имеет связанной привычки и вознаграждения."""

    def __call__(self, attrs):
        if attrs.get("is_joy"):
            if attrs.get("joy_habit") or attrs.get("reward"):
                raise ValidationError("У приятной привычки не может быть "
                                      "вознаграждения или другой связанной "
                                      "приятной привычки")


class HabitHaveJoyHabitOrReward:
    """
    Класс валидатора. Проверяет, что у полезной привычки заполнено только одно из
    полей: либо поле связанной привычки, либо поле вознаграждения.
    """

    def __call__(self, attrs):
        if attrs.get("is_joy") is False:
            if attrs.get("joy_habit") and attrs.get("reward"):
                raise ValidationError("Должно быть заполнено либо поле приятной "
                                      "привычки, либо поле вознаграждения")


class IsJoyHabitForJoyHabitField:
    """Класс валидатора. Проверяет, что связанная привычка является приятной."""

    def __call__(self, attrs):
        if attrs.get("joy_habit"):
            if not attrs.get("joy_habit").is_joy:
                raise ValidationError("Связанной может быть только приятная привычка")


class PeriodInDaysNoMoreSeven:
    """Класс валидатора. Проверяет, что периодичность повторения привычки от 1 до 7 дней."""

    def __call__(self, attrs):
        if attrs.get("period_in_days"):
            if attrs.get("period_in_days") > 7:
                raise ValidationError("Периодичность повторения привычки не может быть более 7 дней")
            if attrs.get("period_in_days") < 1:
                raise ValidationError("Периодичность привычки не может быть меньше 1 дня")
