import telebot
from telebot import types
from config import API_token
import time

bot = telebot.TeleBot(API_token)

# Send different media to the user
@bot.message_handler(commands=['start1'])
def send_welcome(message):
    bot.send_photo(message.chat.id, open("", "rb"), caption="")
    bot.send_video(message.chat.id, open("", "rb"), caption="")
    bot.send_document(message.chat.id, open("", "rb"), caption="")
    bot.send_audio(message.chat.id, open("", "rb"), caption="")


# Send chat action to the user
@bot.message_handler(commands=['start2'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, action="upload_video")
    with open("C:/Users/eaca8/Downloads/19.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption="The new video")

# Send multiple photos to the user
media = []
@bot.message_handler(commands=['start3'])
def send_welcome(message):
    p1 = types.InputMediaPhoto(open("C:/Users/eaca8/OneDrive/Pictures/Camera Roll/1.jpg", "rb"))
    p2 = types.InputMediaPhoto(open("C:/Users/eaca8/OneDrive/Pictures/Camera Roll/2.jpg", "rb"))
    media.append(p1)
    media.append(p2)
    bot.send_chat_action(message.chat.id, action="upload_photo")
    bot.send_media_group(message.chat.id, media=media)

bot.polling()