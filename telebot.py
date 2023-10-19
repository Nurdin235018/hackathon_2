import telebot

bot = telebot.TeleBot('6424383237:AAFy6OpLN2AcS8LS6g6HNM5GorcZk121y_Y')


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


bot.polling(none_stop=True)
