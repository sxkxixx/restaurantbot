import telebot
from telebot import types

TOKEN = '5712346447:AAFLnwdYW66Fwt3PzHyiV-j2kJC0O0XyqUY'
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
restaurant_name = '"RESTAURANT_NAME"'

default_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_button = types.KeyboardButton('START')


@bot.message_handler(commands=['start'])
def welcome_message(message):
    username = message.from_user.username
    bot.send_message(message.chat.id,
                     f'Здравствуйте, @{username}. Рады приветствовать в Telegram-Боте ресторана <b>{restaurant_name}</b>. Здесь вы можете посмотреть меню ресторана, забронировать стол и т.д.')


@bot.message_handler(commands=['commands'])
def show_commands(message):
    pass


bot.infinity_polling()
