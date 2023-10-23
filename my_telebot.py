from decouple import config
import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot(config('TOKEN'))

import requests
from io import BytesIO
from parser import chart_data

def handle_start(message):
    response = requests.get('http://localhost:8000/api/bilets/ticket-recommendations/', json=True)
    if response.status_code == 200:
        bot_messages = response.json()
        print(bot_messages)
        if bot_messages is not None:


            for bot_messages in bot_messages:
                title = bot_messages['title']
                location = bot_messages['location']
                price = bot_messages['price']
                description = bot_messages['description']
                date = bot_messages['date']
                total_ticket = bot_messages['total_ticket']
                rating = bot_messages['rating']
                image_url = bot_messages['image']
                like = bot_messages['like_count']

                # Загрузите изображение по URL
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    image_bytes = BytesIO(image_response.content)

                    # Отправьте изображение вместе с текстом
                    bot.send_photo(message.chat.id, image_bytes, caption=f"Исполнитель: {title}\n"
                                                                        f"Цена: {price} сом \n"
                                                                        f"О полете: {description}\n"
                                                                        f"Дата : {date}\n"
                                                                        f"Количество билетов: {total_ticket}\n"
                                                                        f"Рейтинг: {rating}\n"
                                                                        f"Лайки: {like}")
                else:
                    bot.send_message(message.chat.id, 'Не удалось загрузить изображение.')
        else:
            bot.send_message(message.chat.id, 'Данные отсутствуют.')
    else:
        bot.send_message(message.chat.id, 'Не удалось получить данные.')



@bot.message_handler(commands=['chart'])
def send_chart_message(message):
    bot.send_message(message.chat.id, chart_data.replace('.', '\n'))

@bot.message_handler(commands=['bilet'])
def handle_start_post(message):
    handle_start(message)


@bot.callback_query_handler(func=lambda call: call.data == 'chart')
def go_to_music(call):
    send_chart_message(call.message)

@bot.callback_query_handler(func=lambda call: call.data == 'handle_start')
def handle_go_to_tickets(call):
    handle_start(call.message)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('http://localhost:8000/api/bilets/')


@bot.message_handler(commands=['info'])  # Это будет выполняться для всех входящих сообщений
def send_hello(message):
    markup = types.InlineKeyboardMarkup(row_width=4)
    markup.add(types.InlineKeyboardButton('Прасмотр билетов', callback_data='handle_start'))
    markup.add(types.InlineKeyboardButton('Просмотреть чарт', callback_data='chart'))
    bot.send_message(message.chat.id, 'Приветствую', reply_markup=markup)

@bot.message_handler(commands=['site', 'website'])
def site(message):
    bot.send_message(message.chat.id, 'Вот ссылка на сайт: http://localhost:8000/api/tickets/')


@bot.message_handler(commands=['start', 'restart'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Переход на сайт')
    item2 = types.KeyboardButton('Просмотр билетов')
    item3 = types.KeyboardButton('Чарт')
    item4 = types.KeyboardButton('Информация')
    item5 = types.KeyboardButton('start')
    markup.add(item1, item2, item3, item4, item5,)

    sticker_id1 = 'CAACAgIAAxkBAAJC2mUPVYIfcCocJ7DigkzrBKLdEG6uAAJ3AQACIjeOBAAByoq1E8mVsTAE'
    bot.send_sticker(message.chat.id, sticker_id1)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['restart'])
def restart_bot(message):
    bot.send_message(message.chat.id, start_command)


@bot.message_handler(func=lambda message: message.text == 'start')
def start_bot(message):
    start_command(message)


@bot.message_handler(func=lambda message: message.text == 'Переход на сайт')
def view_website(message):
    site(message)


@bot.message_handler(func=lambda message: message.text == 'Просмотр билетов')
def check(message):
    handle_start(message)


@bot.message_handler(func=lambda message: message.text == 'Чарт')
def music_chart(message):
    send_chart_message(message)

@bot.message_handler(func=lambda message: message.text == 'Информация')
def informate(message):
    send_hello(message)


bot.polling(none_stop=True)