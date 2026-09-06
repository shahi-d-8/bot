import requests
import telebot

TOKEN ="8799777541:AAHPqdt7Edl1CosHdJaHQms9h0U9tcAyPro"
API_KEY = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE4MjAyMDY4NTQsImlhdCI6MTc4ODY3MDg1NCwicmF5IjoiNzMxYTUxYzkyYWMxNjRhMmQ1MzAzYjdlNjRlNGM3OWMiLCJzdWIiOjQ1MDY2OTV9.ZFCMj_T3pfFT-MC6MtlgDJoQLUw4BvXYX7DiGRgnGA2WYDTa3yST_WcOYGHp1aqbf04-pKvLRJ4egTzxEfgbeKpIU9siQKuLuYRirMJ5LEJeIwdVvSfHQUe2P3gk1JRbyyoNsdlTQm6J-cTbqRIu-QkBRybvUMy5WPdDxZg66eiOGD9Fsx3sgJKs-n5iczQXnlXf2IJsz5j7IU-HnDjMP362ws_VRpI-Kjg_MC2vgaq_a2WR1m9Fo1bXC7P-aJX8sevYVvtWJ_T0S6z5f9P0SmlyIQeXq_Bo2_fTUJ539YJ22JLiU2tzXrmDxGsdc_XgL5MkuxiJ073CTnb242aDJw"
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
