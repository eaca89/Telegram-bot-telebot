from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup						   

from telebot import TeleBot
from config import API_token

bot = TeleBot(API_token)

# Defining and adding buttons 
button1 = InlineKeyboardButton(text="button1", callback_data="In_First_button") 
button2 = InlineKeyboardButton(text="button2", callback_data="In_Second_button") 
keyboard_inline = InlineKeyboardMarkup().add(button1, button2) 

# Message handler for the /button1 command 
@bot.message_handler(commands=['start']) 
def check(message): 
	bot.reply_to(message, "hi! how are you", reply_markup=keyboard_inline) 

# Callback query handler for the inline keyboard buttons 
@bot.callback_query_handler(func=lambda call:True) 
def check_button(call): 
	# Checking which button is pressed and respond accordingly 
	if call.data == "In_First_button": 
		bot.answer_callback_query(call.id,"Hi! This is the first inline keyboard button.", show_alert=True) 
	if call.data == "In_Second_button": 
		bot.answer_callback_query(call.id,"Hi! This is the second inline keyboard button.", show_alert=True) 
	

# Start the bot 
bot.polling() 
