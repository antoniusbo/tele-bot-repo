def welcome_message(bot, message):
    with open('sticker.webp', 'rb') as welcome_sticker:
        bot.send_sticker(message.chat.id, welcome_sticker)

        bot.send_message(message.chat.id, f"\
        Hi there, {message.from_user.first_name} {message.from_user.last_name}! I am your Bot. I am here to try and test the functionality of Python and the Telegram library and acquire the necessary knowledge and experience.")

# @bot.message_handler(commands=['help'])
def help_instruction(bot, message):
    instructions = 'bot_instructions.txt'
    with open(instructions, 'r') as file:
        content = file.read()

        bot.send_message(message.chat.id, f'The bot instructions are:\n\n{content}')