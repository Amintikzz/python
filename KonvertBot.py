import telebot
from telebot import types

valuta1 = ''
valuta2 = ''
summa = 0

bot = telebot.TeleBot('8132968885:AAGAhdzJQBNSwM06cMbbHQ0n6F9zQpSusv4')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('тенге')
    itembtn2 = types.KeyboardButton('рубль')
    itembtn3 = types.KeyboardButton('доллар')
    itembtn4 = types.KeyboardButton('евро')
    markup.add(itembtn1,itembtn2,itembtn3,itembtn4)
    mess = f'Салам алейкум, {message.from_user.first_name}\nВведите вашу валюту:'
    bot.send_message(message.from_user.id, mess, reply_markup=markup)
    bot.register_next_step_handler(message, ryzen)


@bot.message_handler(content_types=['text'])
def ryzen(message):
    global valuta1
    valuta1 = message.text
    bot.send_message(message.from_user.id, 'Введите валюту для конвертации:')
    bot.register_next_step_handler(message, lion)

@bot.message_handler(content_types=['text'])
def lion(message):
    global valuta2
    valuta2 = message.text
    bot.send_message(message.from_user.id, 'Введите сумму:')
    bot.register_next_step_handler(message, konvert)

@bot.message_handler(content_types=['text'])
def konvert(message):
    global summa
    global valuta1
    global valuta2
    summa = int(message.text)
    if valuta1 == 'тенге' and valuta2 == 'рубль':
        bot.send_message(message.from_user.id, summa/5)
    elif valuta1 == 'тенге' and valuta2 == 'доллар':
        bot.send_message(message.from_user.id, summa/500)
    elif valuta1 == 'тенге' and valuta2 == 'евро':
        bot.send_message(message.from_user.id, summa/600)
    elif valuta1 == 'рубль' and valuta2 == 'тенге':
        bot.send_message(message.from_user.id, summa*5)
    elif valuta1 == 'рубль' and valuta2 == 'доллар':
        bot.send_message(message.from_user.id, summa/80)
    elif valuta1 == 'рубль' and valuta2 == 'евро':
        bot.send_message(message.from_user.id, summa/100)
    elif valuta1 == 'доллар' and valuta2 == 'тенге':
        bot.send_message(message.from_user.id, summa*500)
    elif valuta1 == 'доллар' and valuta2 == 'рубль':
        bot.send_message(message.from_user.id, summa*80)
    elif valuta1 == 'доллар' and valuta2 == 'евро':
        bot.send_message(message.from_user.id, summa/1.14)
    elif valuta1 == 'евро' and valuta2 == 'тенге':
        bot.send_message(message.from_user.id, summa*600)
    elif valuta1 == 'евро' and valuta2 == 'рубль':
        bot.send_message(message.from_user.id, summa*90)
    elif valuta1 == 'евро' and valuta2 == 'доллар':
        bot.send_message(message.from_user.id, summa*1.14)
        



bot.polling(none_stop=True, interval=0)


    
