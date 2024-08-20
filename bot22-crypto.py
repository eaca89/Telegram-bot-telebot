from config import API_token
import telebot
import requests
import matplotlib.pyplot as plt
import io
from datetime import datetime

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your bot's token
bot = telebot.TeleBot(API_token)

# Function to get historical data for the last 24 hours
def get_histo_minute(symbol, limit=1440):
    url = f'https://min-api.cryptocompare.com/data/v2/histominute'
    params = {
        'fsym': symbol,
        'tsym': 'USD',
        'limit': limit,
        'aggregate': 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['Response'] == 'Success':
        return data['Data']['Data']
    else:
        return None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome! Send me a cryptocurrency symbol (e.g., BTC) to get its latest stats.")

@bot.message_handler(func=lambda message: True)
def get_crypto_price(message):
    crypto_symbol = message.text.upper()
    price_data = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={crypto_symbol}&tsyms=USD').json()
    
    if 'USD' not in price_data:
        bot.reply_to(message, "🚫 Sorry, I couldn't find the price for that cryptocurrency.")
    else:
        # Get detailed data (high, low, etc.) for the last 24 hours
        detailed_data = requests.get(
            f'https://min-api.cryptocompare.com/data/generateAvg?fsym={crypto_symbol}&tsym=USD&e=CCCAGG'
        ).json()

        price = price_data['USD']
        high = detailed_data['DISPLAY']['HIGH24HOUR']
        low = detailed_data['DISPLAY']['LOW24HOUR']
        change = detailed_data['DISPLAY']['CHANGE24HOUR']
        change_pct = detailed_data['DISPLAY']['CHANGEPCT24HOUR']
        volume = detailed_data['DISPLAY']['VOLUME24HOUR']

        response = (
            f"💰 *{crypto_symbol} Stats:*\n\n"
            f"🔹 *Price*: ${price:.2f} USD\n"
            f"📈 *24h High*: ${high} USD\n"
            f"📉 *24h Low*: ${low} USD\n"
            f"🔄 *24h Change*: ${change} USD ({change_pct}%)\n"
            f"📊 *24h Volume*: {volume} {crypto_symbol}"
        )
        
        bot.reply_to(message, response, parse_mode='Markdown')

        # Get historical data for the last 24 hours (1440 minutes)
        histo_data = get_histo_minute(crypto_symbol)
        
        if histo_data:
            times = [datetime.fromtimestamp(item['time']) for item in histo_data]
            prices = [item['close'] for item in histo_data]

            # Create the price variation chart
            fig, ax = plt.subplots()
            ax.plot(times, prices, color='skyblue')
            ax.set_xlabel('Time')
            ax.set_ylabel('Price in USD')
            ax.set_title(f'{crypto_symbol} Price Variation (Last 24 Hours)')
            fig.autofmt_xdate()

            # Save plot to a bytes buffer
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)

            # Send the chart as an image
            bot.send_photo(message.chat.id, buf)
        else:
            bot.reply_to(message, "⚠️ Could not retrieve historical data.")

bot.polling()
