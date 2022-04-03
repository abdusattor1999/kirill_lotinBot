from transliterate import to_cyrillic , to_latin
import telebot

TOKEN = '5175327304:AAHlXUYbbqgiYUqN_xHYEWyaB-KwcBXRx98'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu Alaykum, Hush kelibsiz !"
    javob += "Matnni kiriting : "
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    xabar = message.text
    if xabar.isascii():
        javob = to_cyrillic(xabar)
    else :
        javob = to_latin(xabar)

    bot.reply_to(message, javob)

bot.polling()


