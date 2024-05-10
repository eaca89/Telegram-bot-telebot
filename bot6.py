from telebot import TeleBot
from config import API_token

bot = TeleBot(API_token)

user_ID = []

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "welcome to microlearn Bot.")
    if message.chat.id not in user_ID:
        user_ID.append(message.chat.id)


@bot.message_handler(commands=['SUPU2024'])
def send_update(message):
    for id in user_ID:
        bot.send_message(id, "The product is available.")

bot.polling()





