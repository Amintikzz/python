import telebot
from telebot import types
import random
import time

bot = telebot.TeleBot('8053638404:AAHES7HJp8fVnS_z76b2hJsxp4rUnmf5bUs')

num1 = 0
num2 = 0

@bot.message_handler(commands=['start'])
def start(message):
    global num1
    global num2
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)

    mess = f'Salem,{message.from_user.first_name}{message.from_user.last_name}!\n{num1}*{num2} = '
    bot.send_message(message.from_user.id, mess)

    var = [num1*num2, random.randint(1,100), random.randint(1,100), random.randint(1,100)]
    random.shuffle(var)
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton(var[0])
    itembtn2 = types.KeyboardButton(var[1])
    itembtn3 = types.KeyboardButton(var[2])
    itembtn4 = types.KeyboardButton(var[3])
    markup.add(itembtn1,itembtn2,itembtn3,itembtn4)
    bot.send_message(message.from_user.id, 'Выбери ответ:', reply_markup=markup)
    bot.register_next_step_handler(message, answer)


@bot.message_handler(content_types=['text'])
def answer(message):
    global num1
    global num2
    n = int(message.text)
    if num1*num2 == n:
        bot.send_message(message.from_user.id,'ай красавчик, а это осилишь?')
    else:
        bot.send_message(message.from_user.id, f'Иди учись аболтус! Правильный ответ:{num1*num2}')

    num1 = random.randint(1,9)
    num2 = random.randint(1,9)

    var = [num1*num2, random.randint(1,100),random.randint(1,100),random.randint(1,100)]
    random.shuffle(var)
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton(var[0])
    itembtn2 = types.KeyboardButton(var[1])
    itembtn3 = types.KeyboardButton(var[2])
    itembtn4 = types.KeyboardButton(var[3])

    markup.add(itembtn1,itembtn2,itembtn3,itembtn4)
    time.sleep(0.5)
    bot.send_message(message.from_user.id,f'{num1}*{num2}=',reply_markup = markup)

bot.polling(none_stop=True, interval=0)




