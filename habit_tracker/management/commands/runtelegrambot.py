from django.core.management.base import BaseCommand
from habit_tracker.external_api_telegram import bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot.infinity_polling()
