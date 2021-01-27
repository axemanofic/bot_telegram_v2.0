from bot_keyboards.keyboard import getKeyboardSummary
from global_var import TEMPLATE_TEXT
from misc import bot


@bot.callback_query_handler(func=lambda c: True)
def callback_query(call):
    bot.edit_message_text(TEMPLATE_TEXT[call.data], disable_web_page_preview=True, chat_id=call.message.chat.id,
                          message_id=call.message.id, reply_markup=getKeyboardSummary(call.data))
