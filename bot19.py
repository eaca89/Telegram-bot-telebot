import telebot
from config import API_token
from datetime import datetime, timedelta

bot = telebot.TeleBot(API_token)

# Type /admin in the group
@bot.message_handler(commands=['admin'])
def get_admin(message):
    admin_list = bot.get_chat_administrators(message.chat.id)
    for item in admin_list:
        print(item.user.username)

@bot.message_handler(commands=['info'])
def get_info(message):
    item1 = bot.get_chat(message.chat.id)
    item2 = bot.get_chat_member(message.chat.id, message.from_user.id)
    item3 = bot.get_chat_member_count(message.chat.id)
    item4 = bot.get_chat_members_count(message.chat.id)

    print(item1)
    print("###########")
    print(item2)
    print(item3)
    print(item4)


@bot.message_handler(commands=['link'])
def build_link(message):
    link = bot.create_chat_invite_link(message.chat.id, )

@bot.channel_post_handler(content_types=['text', 'audio', 'video', 'document', 'photo', 'sicker', 'voice', 'contact', 'location'])
def forward_message(message):
    channel1 = ""
    channel2 = ""

    bot.forward_message(
        chat_id= channel1,
        from_chat_id=channel2,
        message_id = message.message_id,
        protect_content=True
    )

    bot.copy_message(
        chat_id= channel1,
        from_chat_id=channel2,
        message_id = message.message_id 
    )

bot.polling()