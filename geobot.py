import math
import telebot
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton(text='Прямая геодезическая задача на плоскости', callback_data='btn1')
    btn1 = types.InlineKeyboardButton(text='Обратная геодезическая задача на плоскости', callback_data='btn2')
    btn2 = types.InlineKeyboardButton(text='Прямая геодезическая задача на сфере', callback_data='btn3')
    btn3 = types.InlineKeyboardButton(text='Обратная геодезическая задача на сфере', callback_data='btn4')
    btn4 = types.InlineKeyboardButton(text='Прямая геодезическая задача на эллипсоиде', callback_data='btn5')
    btn5 = types.InlineKeyboardButton(text='Обратная геодезическая задача на эллипсоиде', callback_data='btn6')
    kb.add(btn, btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, 'Решение геодезических задач', reply_markup=kb)

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        bot.send_message(callback.message.chat.id,'Решаем прямую геодезическую задачу на плоскости')
        sent1 = bot.send_message(callback.message.chat.id, 'Введите через запятую\nРасстояние, Дирекционный угол, Координату X1, Координату Y1:\nS,Ang,X1,Y1')
        bot.register_next_step_handler(sent1, directTask)
    if callback.data == 'btn2':
        bot.send_message(callback.message.chat.id, 'Решаем обратную геодезическую задачу на плоскости')
        sent1 = bot.send_message(callback.message.chat.id, 'Введите через запятую\nКоординату X1, Координату Y1, Координату X2, Координату Y2:\nX1,Y1,X2,Y2')
        bot.register_next_step_handler(sent1, inverseTask)
    if callback.data == 'btn3':
        bot.send_message(callback.message.chat.id, 'Решаем прямую геодезическую задачу на сфере')

def directTask(message):
    # input
    user_message = message.text
    args = user_message.split(',')

    # parsing
    S = float(args[0])
    Ang = float(args[1])
    X1 = float(args[2])
    Y1 = float(args[3])

    # calculations
    X2 = X1 + S * math.cos(Ang * math.pi / 180)
    Y2 = Y1 + S * math.sin(Ang * math.pi / 180)
    print('Дано:', 'S =', S, '; Ang =', Ang, '; X1 =', X1, '; Y1 =', Y1)
    print('Решение:', 'X2 =', X2, '; Y2 =', Y2)

    # output
    task = 'Дано: S =' + str(S) + '; Ang =' + str(Ang) + '; X1 =' + str(X1) + '; Y1 =' + str(Y1)
    solution = '\nРешение: ' + 'X2 =' + str(X2) + '; Y2 =' + str(Y2)
    bot.send_message(message.chat.id, task + solution)

def inverseTask(message):
    # input
    user_message = message.text
    args = user_message.split(',')

    # parsing
    X1 = float(args[0])
    Y1 = float(args[1])
    X2 = float(args[2])
    Y2 = float(args[3])

    # TODO calculations

bot.polling()

