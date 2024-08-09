import telebot
from config import API_token
from datetime import datetime, timedelta

bot = telebot.TeleBot(API_token)

@bot.message_handler(func=lambda message: message.startwith("silence"))
def mute_user(message):
    duration = message.text.split()[-1]
    date = datetime.now() + timedelta(minutes=duration)
    until_date = int(datetime.timestamp(date))

    bot.restrict_chat_member(
        message.chat.id, message.reply_to_message.from_user.id,
        until_date=until_date,
        can_send_media_messages=False,
        can_send_messages=False,
        can_send_other_messages=False,
        can_send_polls=False
    )
    bot.reply_to(message, f"The user is silencee for {duration}")


@bot.message_handler(func=lambda message: message.startwith("ban"))
def mute_user(message):
    duration = message.text.split()[-1]
    date = datetime.now() + timedelta(minutes=duration)
    until_date = int(datetime.timestamp(date))

    bot.ban_chat_member(
        message.chat.id, message.reply_to_message.from_user.id,
        until_date=until_date,        
    )
    bot.reply_to(message, f"The user is banned for {duration}")


@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    bot.reply_to(message, f'user{message.form_user.first_name}\nwelcome to the group.')

bot.polling()