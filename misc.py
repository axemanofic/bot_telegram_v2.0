from telebot import TeleBot
from config import TOKEN, WEBHOOK_HOST

bot = TeleBot(TOKEN, parse_mode='HTML')
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_HOST.format(TOKEN))
