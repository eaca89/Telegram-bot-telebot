import telebot, time
from telebot import types
from config import API_token

bot = telebot.TeleBot(API_token)

my_photo = open("C:/Users/eaca8/OneDrive/Pictures/Camera Roll/1.jpg", "rb")
my_video = open("C:/Users/eaca8/Downloads/19.mp4", "rb")
                
@bot.message_handler(commands=['start'])
def send_welcome(message):
    m1 = bot.send_message(message.chat.id, text="Welcome to the Bot!")
    m2 = bot.send_photo(message.chat.id, photo=my_photo, caption="The first caption")
    time.sleep(3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=m1.message_id, text="متن ادیت شده است")
    # bot.edit_message_caption(chat_id=message.chat.id, message_id=m2.message_id, caption="کپشن جدید")    
    bot.send_chat_action(message.chat.id, action="upload_video")
    bot.edit_message_media(chat_id=message.chat.id, message_id=m2.message_id, media=types.InputMediaVideo(my_video, caption="یه ویدیو آپلود شد"))


@bot.message_handler(commands=['help'])
def send_help(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("button", callback_data="btn1")
    markup.add(button)
    bot.send_photo(message.chat.id, photo=my_photo, caption="text", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "btn1")
def query_handler(call):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("دکمه جدید", callback_data="btn2")
    markup.add(button)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)


bot.polling()
