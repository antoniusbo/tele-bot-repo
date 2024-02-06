import requests
import json
import config

# import config

# @bot.message_handler(text=['weather'])
def weather_input(bot, message, API):
    city = message.text.strip().lower()
    success, temp = get_weather(city, API)
    if success:
        bot.reply_to(message, f'The weather now is: {temp}°C')
    else:
        bot.reply_to(message, f'City is not correctly written.')

# bot.message_handler(content_types=['text'])
def get_weather(city, API):
     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
     if res.status_code == 200: # 200 means a successful url processing
          data = json.loads(res.text)
          temp = data["main"]["temp"]
          return True, temp
     else:
          return False, None