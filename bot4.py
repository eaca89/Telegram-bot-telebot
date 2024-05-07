import telebot
from config import API_token

bot = telebot.TeleBot(API_token)

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
  pass

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    if message.audio:
        bot.reply_to(message, "This is an audio file")
    
    elif message.document:
        bot.reply_to(message, 'This is a document file')

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="2024")
def handle_message(message):
  bot.reply_to(message, "This message contains 2024")

# Handles all messages for which the lambda returns True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
  bot.reply_to(message, "This is a text file")

# Which could also be defined as:
def test_message(message):  
  return message.document.mime_type == 'text/plain'

@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
  bot.reply_to(message, "This is a text file...")

# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji
@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda msg: msg.text == "😂")
def send_something(message):
    bot.reply_to(message, 'Emoji')

bot.polling()