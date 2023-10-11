import webbrowser
import requests
import telebot
from telebot import types
from github import Github
github_token = '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'
github_username = 'Suprrllys'
repo_name = 'shok1chBot'
bot = telebot.TeleBot('6440865768:AAEOjUz49CQ5qrwnQ7x3xXhNf8OhyCRbIQ4')
is_bot_active = False

@bot.message_handler(commands=['start'])
def start(message):
    global is_bot_active
    is_bot_active = True
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    item1 = types.KeyboardButton("/start")
    item2 = types.KeyboardButton("/help")
    item3 = types.KeyboardButton("/source")
    item4 = types.KeyboardButton("/image")
    item5 = types.KeyboardButton("/audio")
    item6 = types.KeyboardButton("/stop")
    markup.add(item1, item2, item3, item4, item5, item6)
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['source'])
def source(message):
    global is_bot_active
    if (is_bot_active):
        bot.send_message(message.chat.id, f'Вы были перенаправлены на веб-страницу. Если вдруг этого не произошло, пожалуйста, нажмите на ссылку: <a>https://github.com/Suprrllys/shok1chBot/blob/main/main.py</a>', parse_mode='html')
        webbrowser.open('https://github.com/Suprrllys/shok1chBot/blob/main/main.py')

@bot.message_handler(commands=['link'])
def link(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти по ссылке", url="http://chelzoo.ru/animals/redbook/mezhdunarodnaya-krasnaya-kniga/"))
    bot.send_message(message.chat.id, 'Красная книга', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    global is_bot_active
    if (is_bot_active):
        bot.send_message(message.chat.id, f'<b>Доступные команды:</b> \n \
        /start - Начать взаимодействие с ботом.\n \
        /help - Показать список доступных команд и их описания.\n \
        /source - Получить ссылку на исходный код бота.\n \
        /image - Получить изображение из репозитория.\n \
        /audio - Получить аудио из репозитория.\n \
        /stop - Остановить бота.', parse_mode='html')

@bot.message_handler(commands=['image', 'audio'])
def get_file(message):
    global is_bot_active
    if (is_bot_active):
        try:
            g = Github(github_token)
            repo = g.get_user(github_username).get_repo(repo_name)
            file_name = ''
            if message.text.startswith("/image"):
                file_number = message.text.split()[-1]
                if file_number in ["1", "2", "3"]:
                    file_name = f"image{file_number}.jpg"
                else:
                    bot.reply_to(message, "Неправильный номер файла. Используйте /image 1, /image 2 или /image 3.")
            elif message.text.startswith("/audio"):
                file_number = message.text.split()[-1]
                if file_number in ["1", "2", "3"]:
                    file_name = f"audio{file_number}.mp3"
                else:
                    bot.reply_to(message, "Неправильный номер файла. Используйте /audio 1, /audio 2 или /audio 3.")
            if file_name:
                file_contents = repo.get_contents(file_name)
                if file_contents:
                    file_url = file_contents.download_url
                    if message.text.startswith("/image"):
                        bot.send_photo(message.chat.id, requests.get(file_url).content)
                    elif message.text.startswith("/audio"):
                        bot.send_audio(message.chat.id, requests.get(file_url).content)
                else:
                    bot.reply_to(message, "Файл не найден в репозитории.")
        except Exception as e:
            bot.reply_to(message, f"Произошла ошибка: {str(e)}")

# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Привет":
#         bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')

@bot.message_handler(commands=['stop'])
def stop(message):
    global is_bot_active
    is_bot_active = False
    bot.send_message(message.chat.id, 'Бот остановлен')

    # else:
    #     bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')

# @bot.message_handler(commands=['link'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Перейти по ссылке", url="http://chelzoo.ru/animals/redbook/mezhdunarodnaya-krasnaya-kniga/"))
#     bot.send_message(message.chat.id, 'Перейдите по ссылке', reply_markup=markup)

bot.polling(none_stop=True)