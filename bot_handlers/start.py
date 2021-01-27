from telebot import types
from bot_keyboards.keyboard import getReplyKeyboard
from db import manage_db
from global_var import TEMPLATE_TEXT
from misc import bot


@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    manage_db.insert_data((message.chat.id, message.chat.first_name))
    bot.send_message(message.chat.id, TEMPLATE_TEXT['welcome'],
                     reply_markup=getReplyKeyboard(TEMPLATE_TEXT['user_button'],
                                                   resize_keyboard=True, one_time_keyboard=True))
