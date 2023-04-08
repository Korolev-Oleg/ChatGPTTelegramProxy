import telebot
from dotenv import dotenv_values
from loguru import logger

import services

config = {**dotenv_values(".env")}

bot = telebot.TeleBot(config["TELEGRAM_API_KEY"])


@logger.catch()
@bot.message_handler(commands=["start"])
def registration(message: telebot.types.Message):
    user, is_new_user = services.login.register_user(message.from_user)
    if user.has_access:
        bot.reply_to(
            message,
            "Привет! У вас есть доступ к боту."
        )
    else:
        additional_msg = "Вы зарегистрированы в системе!" if is_new_user else ""
        bot.reply_to(
            message,
            f"Привет! {additional_msg}"
            "для доступа к боту напишите @hustncn",
        )


@logger.catch()
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
