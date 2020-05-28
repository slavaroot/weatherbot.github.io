import telebot
import pyowm

owm = pyowm.OWM('1195a34f05fbee64f2bf544da26f0982')
bot = telebot.TeleBot('857328939:AAErdqGLGe93RRQ40s7ck-KnHO84AVHjoy4')


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']

    answer = 'В городе' + message.text + 'сейчас' + w.get_detailed_status() + '\n'
    answer += 'Температура сейчас в районе ' + str(temp) + '\n\n'
    # bot.reply_to(message, message.text)

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
