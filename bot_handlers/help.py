from telebot import types
from bot_keyboards.keyboard import getReplyKeyboard
from global_var import TEMPLATE_TEXT
from misc import bot


@bot.message_handler(commands=['help'])
def help_command(message: types.Message):
    bot.send_message(message.chat.id, TEMPLATE_TEXT['help'],
                     reply_markup=getReplyKeyboard(TEMPLATE_TEXT['user_button'],
                                                   resize_keyboard=True, one_time_keyboard=True))
