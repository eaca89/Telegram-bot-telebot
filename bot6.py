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


################ Admin Scenario ########################
import telebot

# Initialize your bot
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Define the admin user ID
ADMIN_USER_ID = 'admin_user_id_here'

# Command to be executed only by the admin
@bot.message_handler(commands=['admin_command'])
def admin_command(message):
    if str(message.from_user.id) == ADMIN_USER_ID:
        # Execute admin-only action here
        bot.reply_to(message, "Admin command executed.")
    else:
        bot.reply_to(message, "You are not authorized to execute this command.")

# Handler for broadcasting messages
@bot.message_handler(func=lambda message: str(message.from_user.id) == ADMIN_USER_ID)
def broadcast_message(message):
    # Broadcast message to all subscribers
    subscribers = []  # Replace with your list of subscriber IDs
    for subscriber_id in subscribers:
        bot.send_message(subscriber_id, message.text)

# Start the bot's polling loop
bot.polling()






