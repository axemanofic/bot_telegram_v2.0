from telebot import types

TITLE_BTN = {
    'about_myself': ['О себе', 'about_myself'],
    'skills': ['Навыки', 'skills'],
    'education': ['Образование', 'education']
}


def getReplyKeyboard(text, resize_keyboard=False, one_time_keyboard=False):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=resize_keyboard,
                                         one_time_keyboard=one_time_keyboard)
    if type(text) == tuple:
        for i in text:
            keyboard.add(types.KeyboardButton(i))
    else:
        keyboard.add(types.KeyboardButton(text))

    return keyboard


def getKeyboardSummary(data):
    buttonlist = list()
    keyboard = types.InlineKeyboardMarkup()

    for i in TITLE_BTN:
        if i == data:
            continue
        buttonlist.append(types.InlineKeyboardButton(TITLE_BTN[i][0], callback_data=TITLE_BTN[i][1]))

    buttonlist.append(types.InlineKeyboardButton("Написать мне", url='https://t.me/axemanofic'))
    buttonlist.append(types.InlineKeyboardButton("GitHub", url='https://github.com/axemanofic'))

    keyboard.row(buttonlist[0], buttonlist[1])
    keyboard.add(buttonlist[2])
    return keyboard
