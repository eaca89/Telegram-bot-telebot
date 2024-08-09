import telebot
from config import API_token

bot = telebot.TeleBot(API_token)

@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    bot.reply_to(message, f'user{message.form_user.first_name}\nwelcome to the group.')


bot.chat_join_request_handler(func=lambda request:True)
def approve(request):
    bot.approve_chat_join_request(request.chat.id, request.from_user.id)
    bot.reply_to(request, f'user {request.from_user.first_name}\n is accepted in the group.')


bot.message_handler(func=lambda message:message.text == 'pin')
def pin(message):
    bot.pin_chat_message(message.chat.id, message.reply_to_message.id)
    bot.reply_to(message, "The message is pinned.")

@bot.message_handler(func=lambda message: message.text == 'add an admin')
def promote(message):
    bot.promote_chat_member(
        message.chat.id,
        message.reply_to_message.json['from']['id'],
        can_change_info=True,
        can_delete_messages=True,
        can_edit_messages=True,
        can_invite_users=True,
        can_manage_chat=True,
        can_manage_topics=True,
        can_manage_video_chats=True,
        can_manage_voice_chats=True,
        can_pin_messages=True,
        can_promote_members=True,
        can_restrict_members=True
    )

@bot.message_handler(func=lambda message: message.text == 'remove an admin')
def demote(message):
    bot.promote_chat_member(
        message.chat.id,
        message.reply_to_message.json['from']['id'],
        can_change_info=True,
        can_delete_messages=True,
        can_edit_messages=True,
        can_invite_users=True,
        can_manage_chat=True,
        can_manage_topics=True,
        can_manage_video_chats=True,
        can_manage_voice_chats=True,
        can_pin_messages=True,
        can_promote_members=True,
        can_restrict_members=True
    )

@bot.message_handler(func=lambda message: message.text == 'ban')
def ban(message):
    bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.reply_to(message, f'The user {message.reply_to_message.from_user.id} is banned.')

@bot.message_handler(func=lambda message: message.text == 'unban')
def unban(message):
    bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.reply_to(message, f'The user {message.reply_to_message.from_user.id} is unbanned.')

@bot.message_handler(func= lambda message: message.text == 'silence')
def restrict(message):
    bot.restrict_chat_member(
        message.chat.id, 
        message.reply_to_message.from_user.id,
        can_add_web_page_previews=True,
        can_change_info=True,
        can_invite_users=True,
        can_pin_messages=True,
        can_send_media_messages=True,
        can_send_messages=True,
        can_send_other_messages=True,
        can_send_polls=True,                             
    )
    bot.reply_to(message, "The user is silenced")

@bot.message_handler(func= lambda message: message.text == 'unsilence')
def derestrict(message):
    bot.restrict_chat_member(
        message.chat.id, 
        message.reply_to_message.from_user.id,
        can_add_web_page_previews=True,
        can_change_info=True,
        can_invite_users=True,
        can_pin_messages=True,
        can_send_media_messages=True,
        can_send_messages=True,
        can_send_other_messages=True,
        can_send_polls=True,                             
    )
    bot.reply_to(message, "The user is unsilenced")

bot.polling()