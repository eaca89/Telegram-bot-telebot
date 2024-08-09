import telebot
from config import API_token
from datetime import datetime, timedelta

bot = telebot.TeleBot(API_token)

@bot.message_handler(commands=['start'])
def welcome(message):
    text1 = "<b>welcome to microlearn Bot.</b>"
    text2 = "<i>welcome to microlearn Bot.</i>"
    text3 = "<code>welcome to microlearn Bot.</code>"
    text4 = "<ins>welcome to microlearn Bot.</ins>"
    text5 = "<s>welcome to microlearn Bot.</s>"
    text6 = "||spoiler||"
    text7 = "[w3school](https://arstechnica.com/gadgets/2024/08/qualcomm-promises-700-arm-powered-pcs-are-coming-sometime-in-2025/)"
    bot.send_message(message.chat.id, text=text1, parse_mode="HTML")
    bot.send_message(message.chat.id, text=text2, parse_mode="HTML")
    bot.send_message(message.chat.id, text=text3, parse_mode="HTML")
    bot.send_message(message.chat.id, text=text4, parse_mode="HTML")
    bot.send_message(message.chat.id, text=text5, parse_mode="HTML")
    bot.send_message(message.chat.id, text=text6, parse_mode="MarkdownV2")
    bot.send_message(message.chat.id, text=text7, parse_mode="MarkdownV2")
    bot.send_message(message.chat.id, text=text7, parse_mode="MarkdownV2", disable_web_page_preview=True)

bot.polling()