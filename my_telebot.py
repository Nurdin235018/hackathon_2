import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config

bot = telebot.TeleBot(config('TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет <b>{message.from_user.first_name}<u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == 'привет' or 'здравствуйте':
        bot.send_message(message.chat.id, "Здравствуйте на нашу Avia Sales."
                                          "Через эту ссылку вы можете подробнее получать информацию о нашей компании",
                         parse_mode='html')
    elif message.text == '':
        bot.send_message(message.chat.id, f"Твой ID:{message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я тебе не понимаю", parse_mode='html')


@bot.message_handler(func=lambda message: message.text == 'buttons')
def get_buttons(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('button1')
    button2 = KeyboardButton('button2')
    keyboard.add(button1, button2)

    bot.send_message(message.chat.id, "Click me", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'button1')
def inline_buttons(message:Message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('hello', callback_data='call1')
    button2 = InlineKeyboardButton('goodbye', callback_data='call2')
    keyboard.add(button1, button2)

    bot.reply_to(message, 'take buttons in message', reply_markup=keyboard)



bot.infinity_polling()
