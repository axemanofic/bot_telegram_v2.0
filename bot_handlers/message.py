from main import bot
from telebot import types
from config import MY_ID
from db import manage_db
from global_var import TEMPLATE_TEXT
from bot_keyboards.keyboard import getReplyKeyboard, getKeyboardSummary


@bot.message_handler(content_types=['text'])
def admin_handler(message: types.Message):
    if message.text == TEMPLATE_TEXT['admin_button'] and message.from_user.id == MY_ID:
        num_users = manage_db.count_data()
        bot.send_message(message.chat.id, TEMPLATE_TEXT['statistic'].format(num_users),
                         reply_markup=getReplyKeyboard(TEMPLATE_TEXT['admin_button'], resize_keyboard=True))
    elif message.text == TEMPLATE_TEXT['user_button']:
        bot.send_message(message.chat.id, TEMPLATE_TEXT['about_myself'], disable_web_page_preview=True,
                         reply_markup=getKeyboardSummary('about_myself'))
    else:
        bot.reply_to(message, "Я не понимаю вас!")
