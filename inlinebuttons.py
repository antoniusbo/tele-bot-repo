from telebot import types

# @bot.message_handler(content_types=['video', 'audio', 'voice', 'sticker', 'document', 'photo'])
def create_inline_keyboard():
    inline_keyboard = types.InlineKeyboardMarkup()

    button_delete = types.InlineKeyboardButton('Delete', callback_data='delete')
    inline_keyboard.add(button_delete)

    button_edit = types.InlineKeyboardButton('Edit', callback_data='edit')
    inline_keyboard.add(button_edit)
    # keyboard.row(button_news, button_weather)

    # button_report = types.InlineKeyboardButton('Download the report', callback_data='download')
    # inline_keyboard.add(button_report)
    # # keyboard.row(button_report)

    return inline_keyboard
    # In order to show the buttons when one of the commands is called