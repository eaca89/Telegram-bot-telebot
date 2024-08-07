import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_token

bot = telebot.TeleBot(API_token)

# Define the main menu
def main_menu():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Menu 1', callback_data='menu1')
    button2 = InlineKeyboardButton('Menu 2', callback_data='menu2')
    markup.add(button1, button2)
    return markup

# Define the submenus for Menu 1
def submenu1():
    markup = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('Submenu 1-1', callback_data='submenu1-1')
    button2 = InlineKeyboardButton('Submenu 1-2', callback_data='submenu1-2')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, return_button)
    return markup

def submenu1_1():
    markup = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton('Button in 1-1', callback_data='button')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_submenu1')
    markup.add(button, return_button)
    return markup

def submenu1_2():
    markup = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton('Button in 1-2', callback_data='button')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_submenu1')
    markup.add(button, return_button)
    return markup

# Define the submenus for Menu 2
def submenu2():
    markup = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('Submenu 2-1', callback_data='submenu2-1')
    button2 = InlineKeyboardButton('Submenu 2-2', callback_data='submenu2-2')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, return_button)
    return markup

def submenu2_1():
    markup = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton('Button in 2-1', callback_data='button')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_submenu2')
    markup.add(button, return_button)
    return markup

def submenu2_2():
    markup = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton('Button in 2-2', callback_data='button')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_submenu2')
    markup.add(button, return_button)
    return markup

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "You are in main menu. Choose an option:", reply_markup=main_menu())

# Callback query handler
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'menu1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You are in menu1", reply_markup=submenu1())
        
    elif call.data == 'submenu1-1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You are in submenu1-1", reply_markup=submenu1_1())
    
    elif call.data == 'submenu1-2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You are in submenu1-2", reply_markup=submenu1_2())
    
    elif call.data == 'menu2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You are in menu2", reply_markup=submenu2())
    
    elif call.data == 'submenu2-1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You are in submenu2-1", reply_markup=submenu2_1())
    
    elif call.data == 'submenu2-2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You are in submenu2-2", reply_markup=submenu2_2())
    
    elif call.data == 'return_to_main':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You are in main menu. Choose an option:", reply_markup=main_menu())
    
    elif call.data == 'return_to_submenu1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You are in submenu1", reply_markup=submenu1())
    
    elif call.data == 'return_to_submenu2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You are in submenu2", reply_markup=submenu2())

bot.polling()