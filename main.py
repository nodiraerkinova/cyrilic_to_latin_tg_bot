import telebot
from  transliterate import to_cyrillic, to_latin
import transliterate

TOKEN="8689290533:AAHhUC2YNft64jRYIDN7zHyIBg29C675dYU"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alekum, botimizga xush kelibsiz!")    

@bot.message_handler(func=lambda m:True)
def echo_all(message):
     
     text = message.text    
     if text.isascii():       
         bot.reply_to(message,to_cyrillic(text))   
     else:
        bot.reply_to(message, to_latin(text))   


bot.infinity_polling()