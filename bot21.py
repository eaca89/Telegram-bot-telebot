import telebot
from telebot.storage import StateMemoryStorage
from telebot.handler_backends import State, StatesGroup
from telebot import custom_filters
from config import API_token

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(API_token, state_storage=state_storage)

class UserInfo(StatesGroup):
    name = State()
    lastname = State()
    age = State()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "What's your name?")
    bot.set_state(message.from_user.id, UserInfo.name, message.chat.id)    

@bot.message_handler(state=UserInfo.name)
def name(message):
    bot.send_message(message.chat.id, "What's your last name?")
    bot.set_state(message.from_user.id, UserInfo.lastname, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text

@bot.message_handler(state=UserInfo.lastname)
def lastname(message):
    bot.send_message(message.chat.id, "How old are you?")
    bot.set_state(message.from_user.id, UserInfo.age, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['lastname'] = message.text

@bot.message_handler(state=UserInfo.age)
def age(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        bot.send_message(message.chat.id, 
                         f"Your name is {data['name']}\n"
                         f"Your last name is {data['lastname']}\n"
                         f"Your age is {message.text}"
                         )
        
    bot.delete_state(message.from_user.id, message.chat.id)


bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    bot.polling()