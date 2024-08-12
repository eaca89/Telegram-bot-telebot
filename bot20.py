import telebot
from config import API_token
from telebot import types

bot = telebot.TeleBot(API_token)

# Inline query
inline_query_data = [
    {
        "id": str(i),
        "title": f"Title {i}",
        "description": f"Description for item {i}",
        "message": f"Message for item {i}",
        "thumb_url": f"https://example.com/thumb{i}.jpg"
    }
    for i in range(1, 6)
]

@bot.inline_handler(func= lambda query: len(query.query) == 0)
def handle_inline_query(query):
    results = []

    for item in inline_query_data:
        result = types.InlineQueryResultArticle(
            id = item["id"],
            title = item["title"],
            description = item["description"],
            input_message_content = types.InputTextMessageContent(
                message_text = item["message"]
            ),
            thumbnail_url = item["thumb_url"]
        )
        results.append(result)
    
    bot.answer_inline_query(inline_query_id=query.id, results=results)


bot.polling()