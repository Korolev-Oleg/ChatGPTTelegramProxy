import telebot
from dotenv import dotenv_values
from loguru import logger

import services
from db.models import Message

config = {**dotenv_values(".env")}

bot = telebot.TeleBot(config["TELEGRAM_API_KEY"])

services.gpt.init(config["OPENAI_API_KEY"])


@logger.catch()
@bot.message_handler(commands=["start"])
def registration(message: telebot.types.Message):
    user, is_new_user = services.login.register_user(message.from_user)
    if user.has_access:
        bot.reply_to(
            message,
            "Привет! У вас есть доступ к боту. "
            "Задавайте вопросы с умом цена одного вопроса ~	$0.002!",
        )
    else:
        additional_msg = (
            "Вы зарегистрированы в системе!" if is_new_user else ""
        )
        services.chat.send_message_to_user_without_access(
            bot, message, additional_msg
        )


@logger.catch()
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user = services.login.authenticate(message.from_user.username)
    if user.has_access:
        sum_price = 0.002 * Message.get_count(user)
        bot.reply_to(
            message, f"Потрачено ${sum_price}. Запрос обрабатывается..."
        )
        response = services.gpt.get_response(user, message.text)
        bot.reply_to(message, response)
    else:
        services.chat.send_message_to_user_without_access(bot, message, "")


bot.polling()
