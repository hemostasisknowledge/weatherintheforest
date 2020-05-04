import telebot
import pyowm

owm = pyowm.OWM('dd1b79b9daf5ef14480da869906d25fb', Language = "ru")
bot = telebot.TeleBot("1001349502:AAH1pQlC9nshDhO_7hLb2eW5XLoUrda-MzI")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = "In the forest of " + message.text + "there is " + w.get_detailed_status() + "\n"
    answer+= "The temperature is around " + str(temp) + "\n\n"

    if temp < 0:
        answer += "It's cold, warm up!"
    elif temp < 10:
        answer += "It's OK for fur bubbles"
    else:
        answer += "Such a nice day!"

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
