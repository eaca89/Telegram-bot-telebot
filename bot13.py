import telebot
from config import API_token

bot = telebot.TeleBot(API_token)

# Replace with your channel's username (without the @)
CHANNEL_USERNAME = "microlearn_ir"

# Function to check if a user is a member of the channel
def is_user_member(user_id):
    try:
        member = bot.get_chat_member(chat_id=f"@{CHANNEL_USERNAME}", user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
    except Exception as e:
        print(f"Error: {e}")
    return False

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if is_user_member(user_id):
        bot.send_message(message.chat.id, "Welcome to the bot! You are allowed to use this bot.")
    else:
        bot.send_message(message.chat.id, f"You need to join the channel @{CHANNEL_USERNAME} to use this bot.")

# Example command handler
@bot.message_handler(commands=['help'])
def send_help(message):
    user_id = message.from_user.id
    if is_user_member(user_id):
        bot.send_message(message.chat.id, "This is the help message for the bot.")
    else:
        bot.send_message(message.chat.id, f"You need to join the channel @{CHANNEL_USERNAME} to use this bot.")

bot.polling()
