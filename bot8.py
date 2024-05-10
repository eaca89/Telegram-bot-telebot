from telebot import TeleBot
from config import API_token
from telebot.types import ReplyKeyboardMarkup

bot = TeleBot(API_token)

# Creating the reply keyboard 
reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
reply_keyboard.add('button1', 'button2')

# Handling the /start command
@bot.message_handler(commands=['start']) 
def welcome(message): 
	bot.reply_to(message,"Check the following keyboard.", reply_markup=reply_keyboard) 


# Handling all other messages 
@bot.message_handler(func=lambda message: True)
def check_button(message):
	if message.text == 'button1':
		bot.reply_to(message, "button1 is pressed.")
	elif message.text == 'button2':
		bot.reply_to(message, 'button2 is pressed.')
	else:
		bot.reply_to(message, f'Your message is: {message.text}')


# Starting the bot 
bot.polling()