import telebot
from dotenv import dotenv_values

import services

config = {**dotenv_values(".env")}

bot = telebot.TeleBot(config["TELEGRAM_API_KEY"])


@bot.message_handler(commands=["start", "help"])
def send_welcome(message: telebot.types.Message):
    services.login.register_user(message.from_user)
    bot.reply_to(
        message,
        "Привет! Вы зарегистрированные в системе, "
        "для доступа к боту напишите @hustncn",
    )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
