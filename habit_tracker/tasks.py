from celery import shared_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from .external_api_telegram import bot
from .models import Habit
import json


def create_task(habit, period_in_days, in_time, id_chat):
    """Функция создания периодической задачи для отправки уведомления о выполнении привычки."""

    reward_for_habit = habit.joy_habit if habit.joy_habit else habit.reward
    if not reward_for_habit:
        reward_for_habit = "завари себе вкусный чай"
    if isinstance(reward_for_habit, Habit):
        reward_for_habit = f"{reward_for_habit.action}\nМесто: {reward_for_habit.place}"

    text = (f"Ваша привычка ждет выполнения: {habit.action}.\n"
            f"Место: {habit.place}.\n"
            f"Не забудь вознаградить себя за выполнение:\n{reward_for_habit}.\n")

    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=in_time.hour,
        minute=in_time.minute,
        day_of_month=f"*/{period_in_days}",
    )

    PeriodicTask.objects.create(
        crontab=schedule,
        name=f"send_notification_by_habit_{habit.pk}",
        task="habit_tracker.tasks.send_notification",
        args=json.dumps([id_chat, text]),
    )


@shared_task
def send_notification(id_chat, text):
    """Функция-задача для отправки увеломления пользователю."""

    bot.send_message(id_chat, text)
