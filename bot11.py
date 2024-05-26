import telebot
from config import API_token

bot = telebot.TeleBot(token=API_token)

@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for new_member in message.new_chat_members:
        welcome_text = f'🎉 User {message.from_user.first_name}, welcome to the group! 🎉'
        bot.send_message(message.chat.id, text=welcome_text)

def is_user_admin(chat_id, user_id):
    admins = bot.get_chat_administrators(chat_id)
    for admin in admins:
        if admin.user.id == user_id:
            return True
    return False

@bot.message_handler(func=lambda message: message.text == "pin")
def pin_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if is_user_admin(chat_id, user_id):
        if message.reply_to_message:
            bot.pin_chat_message(chat_id, message.reply_to_message.message_id)
            bot.reply_to(message.reply_to_message, "The message is pinnded successfully!")
        else:
            bot.reply_to(message, "Please reply to the message you want to pin.")

    else:
        bot.send_message(message.chat.id, "Only admins can pin messages!")

bot.polling()