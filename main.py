import telebot
from telebot import types

bot = telebot.TeleBot('6440865768:AAEOjUz49CQ5qrwnQ7x3xXhNf8OhyCRbIQ4')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['link'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти по ссылке", url="http://chelzoo.ru/animals/redbook/mezhdunarodnaya-krasnaya-kniga/"))
    bot.send_message(message.chat.id, 'Красная книга', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('/link')
    start = types.KeyboardButton('/start')
    photo = types.KeyboardButton('фото')
    audio = types.KeyboardButton('аудио')
    markup.add(website, start, photo, audio )
    bot.send_message(message.chat.id, 'Красная книга', reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "фото":
        photo = open('upload-20021111_gaf_u43_035-pic_32ratio_600x400-600x400-98006.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "аудио":
        audio = open('ой ёй ёй.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)

    # else:
    #     bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')

# @bot.message_handler(commands=['link'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Перейти по ссылке", url="http://chelzoo.ru/animals/redbook/mezhdunarodnaya-krasnaya-kniga/"))
#     bot.send_message(message.chat.id, 'Перейдите по ссылке', reply_markup=markup)

bot.polling(none_stop=True)