from telebot import TeleBot
from config import API_token
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = TeleBot(API_token)

# Defining and adding buttons 
button1 = InlineKeyboardButton(text="button1", callback_data="btn1")
button2 = InlineKeyboardButton(text="button2", callback_data="btn2")
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard.add(button1, button2)

# Message handler for the /button1 command 
@bot.message_handler(commands=['start'])
def welcome(message):	
		bot.send_message(message.chat.id, "welcome to microlearn Bot.", reply_markup=inline_keyboard)	


# Callback query handler for the inline keyboard buttons 
@bot.callback_query_handler(func=lambda call:True)
def check_button(call):
	if call.data == "btn1":
		bot.answer_callback_query(call.id, "Btn1 is tapped.", show_alert=True)
	elif call.data == "btn2":
		bot.answer_callback_query(call.id, "Btn2 is pressed.")



# Start the bot 
bot.polling()
