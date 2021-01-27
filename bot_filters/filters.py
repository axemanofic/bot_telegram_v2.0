from telebot import types
from config import MY_ID


def admin_filter(message: types.Message):
    if message.from_user.id == MY_ID:
        return True
    else:
        return False
