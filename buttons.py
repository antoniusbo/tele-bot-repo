from telebot import types # for the buttons

# @bot.buttons_handler(commands=['buttons'])
def create_keyboard ():
    # keyboard = types.InlineKeyboardMarkup()
    #
    # button_report = types.InlineKeyboardButton('Download the report', callback_data=None)
    # keyboard.add(button_report)
    # # keyboard.row(button_report)
    #
    # button_news = types.InlineKeyboardButton('News', callback_data=None)
    # # keyboard.add(button_news)
    # button_weather = types.InlineKeyboardButton('Weather', callback_data=None)
    # # keyboard.add(button_weather)
    # keyboard.row(button_news, button_weather)
    #
    # button_game = types.InlineKeyboardButton('Game', callback_data=None)
    # # keyboard.add(button_game)
    # button_cash = types.InlineKeyboardButton('Cash', callback_data=None)
    # # keyboard.add(button_cash)
    # keyboard.row(button_game, button_cash)
    #
    # button_crypto = types.InlineKeyboardButton('Crypto', callback_data=None)
    # keyboard.add(button_crypto)

    keyboard = types.ReplyKeyboardMarkup(row_width=3)

    button_report = types.KeyboardButton('Personal finance report operations')
    button_news = types.KeyboardButton('News')
    button_weather = types.KeyboardButton('Weather', request_location=False)
    #Determines whether the location will be requested from the user when clicking on this button
    #if True then the bot will request the location of the user to determine the weather.
    button_game = types.KeyboardButton('Game')
    button_cash = types.KeyboardButton('Cash')
    button_crypto = types.KeyboardButton('Crypto')
    button_gpd = types.KeyboardButton('Chat GPD')

    keyboard.add(button_report, button_news)
    keyboard.add(button_weather, button_game)
    keyboard.add(button_cash, button_crypto)
    keyboard.add(button_gpd)


    return keyboard
    # In order to show the buttons when one of the commands is called
    # bot.send_message(message.chat.id,
    #                  f'Hello, {message.from_user.first_name} {message.from_user.last_name}! Please choose any of available options',
    #                  reply_markup=keyboard)

# @bot.buttons_handler(commands=['finish'])
def hide_keyboard():
    return types.ReplyKeyboardRemove()