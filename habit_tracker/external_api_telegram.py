from telebot import TeleBot
from config.settings import TELEGRAM_BOT_TOKEN
from users.models import User
from django.core.exceptions import ObjectDoesNotExist


bot = TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    bot.send_message(message.chat.id, "Привет и добро пожаловать в HabitTracker! "
                                      "Познакомимся? Введи почту, с которой "
                                      "зарегистрировался в приложении, чтобы я мог помочь "
                                      "тебе сформировать полезные привычки")
    bot.register_next_step_handler(message, get_email_user)


def get_email_user(message):
    email = message.text
    try:
        user = User.objects.filter(email=email).get()
        user.id_chat_telegram_bot = message.chat.id
        user.save()
        bot.send_message(message.chat.id, "Приятно познакомиться! Теперь я буду отправлять "
                                          "тебе уведомления, чтобы ты не забывал о своих привычках")
    except ObjectDoesNotExist:
        bot.send_message(message.chat.id, "Упс, я не знаю такого email... "
                                          "Давай начнем все с начала, отправь мне '/start'")
