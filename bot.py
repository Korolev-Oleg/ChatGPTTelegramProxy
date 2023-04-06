import requests
import telebot
from dotenv import dotenv_values

config = {
    **dotenv_values(".env")
}

bot = telebot.TeleBot(config["TELEGRAM_API_KEY"])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
