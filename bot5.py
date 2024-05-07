import telebot
from config import API_token

bot = telebot.TeleBot(API_token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Please enter your name:")
    bot.register_next_step_handler(message, process_name)

def process_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Hello {name}! How old are you?")

    bot.register_next_step_handler(message, process_age)

def process_age(message):
    age = message.text
    bot.send_message(message.chat.id, f"You are {age} years old.\nThank you.")

    
bot.polling()