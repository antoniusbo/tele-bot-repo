import telebot
import config
# from content import handle_photo
from commands import welcome_message
from commands import help_instruction
from buttons import create_keyboard
from inline_buttons import create_inline_keyboard
from buttons import hide_keyboard
from weather import weather_input
from config import API
from telebot import types



bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_welcome_message(message):
    welcome_message(bot, message)

@bot.message_handler(commands=['help'])
def handle_help_instruction(message):
    help_instruction(bot, message)

@bot.message_handler(commands=['buttons'])
def handle_buttons(message):
    keyboard = create_keyboard()

    bot.send_message(message.chat.id,
                     f'Hello, {message.from_user.first_name} {message.from_user.last_name}! Please choose any of available options',
                     reply_markup=keyboard)

@bot.message_handler(content_types=['video', 'audio', 'voice', 'sticker', 'document', 'photo'])
def handle_inline_buttons(message):
    inline_keyboard = create_inline_keyboard()

    bot.send_message(message.chat.id,
                     f'{message.from_user.first_name}, What would you like to do with it?', reply_markup=inline_keyboard)

@bot.message_handler(commands=['finish'])
def handle_finish_command(message):
    reply_markup = hide_keyboard()
    bot.send_message(message.chat.id, 'Keyboard is hidden.', reply_markup=reply_markup)

states = {}

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    chat_id = message.chat.id
    # processing of each message
    # WEATHER
    if message.text == "Weather":
        bot.send_message(chat_id, 'Please write down a city here:')
        states[chat_id] = 'weather'
        # weather_input(bot, message)
    #NEWS
    elif message.text == "News":

        markup = types.InlineKeyboardMarkup() #It is in front in order not to determine the cycle for each button, otherwise
        #there will be only the last button shown

        button = types.InlineKeyboardButton("RBC", url='https://www.rbc.ru/')
        markup.add(button)

        button1 = types.InlineKeyboardButton("Forklog", url='https://forklog.com/')
        markup.add(button1)

        button2 = types.InlineKeyboardButton("Sportbox", url='https://news.sportbox.ru/Vidy_sporta/Futbol')
        markup.add(button2)

        bot.send_message(message.chat.id, "Please choose any of available options", reply_markup=markup )

    # CASH
    elif message.text == "Cash":
        cash_markup = types.InlineKeyboardMarkup()
        cash_inflow_button = types.InlineKeyboardButton("Cash Inflow", callback_data="cash_inflow")
        cash_outflow_button = types.InlineKeyboardButton("Cash Outflow", callback_data="cash_outflow")
        cash_markup.add(cash_inflow_button, cash_outflow_button)

        bot.send_message(chat_id, "Please choose an operation with cash:", reply_markup=cash_markup)

    # HERE TO CONTINUE

    #  PERSONAL FINANCE REPORT OPERATIONS
    elif message.text == "Personal finance report operations":
        report_markup = types.InlineKeyboardMarkup()
        report_download_button = types.InlineKeyboardButton("Download", callback_data="report_download")
        report_create_button = types.InlineKeyboardButton("Create", callback_data="report_create")
        report_delete_button = types.InlineKeyboardButton("Delete", callback_data="report_delete")
        report_markup.add(report_download_button, report_create_button, report_delete_button)

        bot.send_message(chat_id, "Please choose an operation with the report:", reply_markup=report_markup)

        # if message.text == "Create":
        #     # bot.send_message(chat_id, 'Cool')
        #     sheet = create_google_sheet()
        #     bot.send_message(chat_id, f"New Google Sheet created with the title: {sheet.title}")


        # HERE TO CONTINUE

    else:
        if chat_id in states and states[chat_id] == 'weather':
            # checks if the value associated with the key chat_id in the states dictionary is equal to the string 'weather'.If the value
            # is 'weather', the condition returns True, otherwise False.
            weather_input(bot, message, API)
            # Сброс состояния пользователя
            del states[chat_id]
            # This operation removes a key - value pair from the dictionary.In this case, when the user completes the weather input,
            # the user's chat_id key state is removed from the states dictionary to reset he state and allow the user to enter new commands.


        else:
            pass

# Callback setup for buttons
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'report_create':
        sheet = create_google_sheet()  # Call the create_google_sheet function
        bot.send_message(callback.message.chat.id, f'Created a new Google Sheet with ID: {sheet.id}')


bot.infinity_polling()