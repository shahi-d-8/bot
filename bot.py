import requests
import telebot

TOKEN = "APNA_TELEGRAM_BOT_TOKEN_YAHAN_LIKHEIN"
API_KEY = "APNA_5SIM_API_KEY_YAHAN_LIKHEIN"
PROFIT_MARGIN = 50

bot = telebot.TeleBot(TOKEN)
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Accept": "application/json"}


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(
      message,
      "خوش آمدید! یہ آپ کا 5sim ری سیلر بوٹ ہے۔\nاکاؤنٹ کا بیلنس چیک کرنے کے"
      " لیے /balance لکھیں۔",
  )


@bot.message_handler(commands=["balance"])
def check_balance(message):
  try:
    url = "https://5sim.net/v1/user/profile"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
      data = response.json()
      balance = data.get("balance", 0)
      bot.reply_to(message, f"آپ کا 5sim اکاؤنٹ بیلنس: {balance}")
    else:
      bot.reply_to(message, "بیلنس چیک کرنے میں خرابی پیش آئی۔ API Key چیک کریں۔")
  except Exception as e:
    bot.reply_to(message, f"خرابی: {str(e)}")


print("Bot is running...")
bot.infinity_polling()
