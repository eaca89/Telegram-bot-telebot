# Importing required libraries 
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup
from config import API_token

bot = TeleBot(API_token)

# Creating the reply keyboard 
keyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard_reply.add("_button1", "_button2") 

# Handling the /start and /help commands 
@bot.message_handler(commands=['start']) 
def welcome(message): 
	# Sending a greeting message that includes the reply keyboard 
	bot.reply_to(message,"Hello! how are you?", reply_markup=keyboard_reply) 


# Handling all other messages 
@bot.message_handler()
def check_rp(message): 

	if message.text == '_button1': 
		# Responding with a message for the first button 
		bot.reply_to(message, "Hi! this is first reply keyboards button.") 

	elif message.text == '_button2': 
		# Responding with a message for the second button 
		bot.reply_to(message, "Hi! this is second reply keyboards button.") 

	else: 
		# Responding with a message that includes the text of the user's message 
		bot.reply_to(message, f"Your message is: {message.text}") 

# Starting the bot 
bot.polling()