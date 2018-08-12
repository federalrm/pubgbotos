
import telebot
from telebot.types import Message
import apiai, json
TOKEN = '628269331:AAGydvEePix6A3LKrxmN1SRG_NGCheAwCCg'
bot = telebot.TeleBot(TOKEN)
bot.polling()
@bot.message_handler(commands=['start'])
def commands_handler(message: Message):
    bot.reply_to(message, 'Привет, я помогу тебе скачать чит для PUBG. Чтобы увидеть список команд введи "/"')
@bot.message_handler(commands=['help'])
def commands_handler(message: Message):
    bot.reply_to(message, 'ESP, RADAR, WH, УБРАТЬ ОТДАЧУ, УБРАТЬ ТЕКСТУРЫ')

    @bot.message_handler(commands=['download'])
    def commands_handler(message: Message):
        bot.reply_to(message, 'Переходи на сайт, нам нем можно узнать всю подробную информацию и скачать сам чит: https://bit.ly/2MIJdPn')

    # Ответ на любое текстовое сообщение
    @bot.message_handler(content_types=['text'])
    # Ответ на любое отредактированное текстовое сообщение
    @bot.edited_message_handler(content_types=['text'])
    def echo_digits(message: Message):
        bot.reply_to(message, "Чтобы увидеть команды, введи /")

bot.polling(timeout=60)
