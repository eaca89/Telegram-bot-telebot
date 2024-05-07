# import requests

# def get_chat_id(bot_token):
#     url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
#     response = requests.get(url)
#     data = response.json()
#     # Extract the chat ID from the latest message
#     chat_id = data['result'][-1]['message']['chat']['id']
#     return chat_id

# # Replace 'YOUR_BOT_TOKEN' with your actual bot token
# bot_token = '7049953760:AAGI98OiR5H7c9EgtRL2lW02tmfkCyBawFI'
# chat_id = get_chat_id(bot_token)
# # print("Chat ID:", chat_id)

# def telegram_bot_sendtext(bot_message):
    
#     bot_token = '7049953760:AAGI98OiR5H7c9EgtRL2lW02tmfkCyBawFI'
#     bot_chatID = '79350183'
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

#     response = requests.get(send_text)

#     return response.json()
    

# test = telegram_bot_sendtext("Testing Telegram bot")
# print(test)

# ############################################


from telebot import TeleBot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = TeleBot('7049953760:AAGI98OiR5H7c9EgtRL2lW02tmfkCyBawFI')

# Define a handler for incoming messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    print(chat_id)
    bot.reply_to(message, f"The chat ID is: {chat_id}")

# Start polling
bot.send_message(79350183, "It's available")
bot.polling()



