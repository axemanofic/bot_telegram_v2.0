from telebot import types
from bot_keyboards.keyboard import getReplyKeyboard
from global_var import TEMPLATE_TEXT
from bot_filters.filters import admin_filter
from misc import bot


@bot.message_handler(func=admin_filter, commands=['admin'])
def start_command(message: types.Message):
    bot.send_message(message.chat.id, 'Добро пожаловать, {}'.format(message.chat.first_name),
                     reply_markup=getReplyKeyboard(TEMPLATE_TEXT['admin_button'], resize_keyboard=True))
