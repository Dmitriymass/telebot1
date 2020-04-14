import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/gif.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")
    item3 = types.KeyboardButton("Какая погода?")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот создан для ответов.".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def lalala(message):
    if message.chat.type == "private":
        if message.text == "Рандомное число":
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "Как дела?":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item3 = types.InlineKeyboardButton("Так себе", callback_data='well')
            item4 = types.InlineKeyboardButton("Великолепно", callback_data='shell')
            item5 = types.InlineKeyboardButton("Что еще надо", callback_data='fell')

            markup.add(item1, item2, item3, item4, item5)
            bot.send_message(message.chat.id, 'Отлично, а у тебя как?', reply_markup=markup)

        elif message.text == "Какая погода?":
            markup = types.InlineKeyboardMarkup(row_width=1)
            item11 = types.InlineKeyboardButton("В Киеве", callback_data='good1')
            item12 = types.InlineKeyboardButton("В другом городе", callback_data='bad1')
            markup.add(item11, item12)
            bot.send_message(message.chat.id, 'В каком городе?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить, но подумаю над твоим вопросом.')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько, поздравляю')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает, но бывает и лучше')

            elif call.data == 'well':
                bot.send_message(call.message.chat.id, 'Что тeбе еще хочется?')

            elif call.data == 'shell':
                bot.send_message(call.message.chat.id, 'Наверное о чем-то мечтаешь?')

            elif call.data == 'fell':
                bot.send_message(call.message.chat.id, 'Наверное много хочешь?')

            elif call.data == 'good1':
                bot.send_message(call.message.chat.id, 'Солнечно')

            elif call.data == 'bad1':
                bot.send_message(call.message.chat.id, 'Сейчас гляну')

            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как дела?",reply_markup=None)

            # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Это тестовое уведомление!!!")
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)

