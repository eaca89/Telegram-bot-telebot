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

# send this command in a group in which the bot is added as an admin
# Type /info in the group
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

# Type /link in the group
@bot.message_handler(commands=['link'])
def build_link(message):
    link = bot.create_chat_invite_link(message.chat.id, )

    """while you can send and interact with bot commands in groups, 
        channels don't support this functionality in the same way.
    """

# This function will be called every time a message is sent in the group
@bot.message_handler(func=lambda message: True, content_types=['text', 'photo', 'video', 'document', 'audio'])
def handle_group_message(message):
    # channel name test 1
    CHANNEL_ID = "-1002204306511"
    # Forward the message to the channel
    bot.forward_message(
        chat_id = CHANNEL_ID, 
        from_chat_id = message.chat.id, 
        message_id = message.message_id)

# This function will be called every time a message is sent in the channel
# @bot.channel_post_handler(func=lambda message: True)
# def handle_channel_post(message):
#     channel_id = message.chat.id
    # print(f"Channel ID: {channel_id}")


# This function forwards every message from channel 1 to channel 2
# @bot.channel_post_handler(content_types=['text', 'audio', 'video', 'document', 'photo', 'sicker', 'voice', 'contact', 'location'])
# def forward_message(message):
#     # channel name test 1
#     channel1 = "-1002204306511"
#     # chennel name test 2
#     channel2 = "-1002246558690"
    

#     bot.forward_message(
#         chat_id= channel1,
#         from_chat_id=channel2,
#         message_id = message.message_id,
#         protect_content=True
#     )

#     bot.copy_message(
#         chat_id= channel1,
#         from_chat_id=channel2,
#         message_id = message.message_id 
#     )

# This function forwards every message from channel 1 to group coditize-GP
# @bot.channel_post_handler(content_types=['text'])
# def get_chat_id(message):
#     bot.reply_to(message, f"Chat ID: {message.chat.id}")
# -1002204306511

# @bot.message_handler(content_types=['text'])
# def get_chat_id(message):
#     bot.reply_to(message, f"group id: {message.chat.id}")
# -4541536669


@bot.channel_post_handler(content_types=['text', 'photo', 'video', 'document', 'audio'])
def forward_post_to_group(message):
    # Replace with the unique IDs for your private channel and group
    CHANNEL_ID = -1002204306511  # The private channel's unique ID, must be a negative number
    GROUP_ID = -4541536669  # The group's unique ID, must be a negative number
    # Forward the message to the group
    bot.forward_message(
        chat_id = GROUP_ID,
        from_chat_id = CHANNEL_ID,
        message_id = message.chat.id
    )

bot.polling()