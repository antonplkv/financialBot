import telebot
from telegramBot import MoneyBot
import config
from checks import *
from utils import *
bot = MoneyBot(config.token)


#Запуск главного меню через комманду старт
@bot.bot.message_handler(commands=["start"])
def start(message):
    dellInfo(message.chat.id)
    setState(message.chat.id,"MainPage/")
    button = ("Потратил бабки :(", "История бабла", "Главная")
    keyboard = bot.get_keyboard(bot.keyboard_tuple(button, 1))
    bot.print_keyboard_message_html(message.chat.id,
                                     "Привет! Я помогу тебе контролировать твои финансы.\nВыбери, что ты хочешь сделать:"
                                     "добавить затрату, либо же просмотреть историю затрат", keyboard)

#Запуск главновго меню через кнопку
@bot.bot.message_handler(func=mainPage)
def start(message):
    setState(message.chat.id,"MainPage/")
    bot.mainMenu(message.chat.id)

#Добавление новых затрат
@bot.bot.message_handler(func=pressedWastedMoney)
def wasted(message):
    setState(message.chat.id,"MainPage/WastedMoney")
    bot.print_message(message.chat.id,"Введи сколько денег ты потратил только что. Я буду суммировать все твои затраты на сегодняшний день")

@bot.bot.message_handler(func=enteredWastedMoney)
def wastedSum(message):
    """Добавляю сумму пользователю устанавливаем состояние на начальную страницу,
    выводим начальную клавиатуру"""
    sumAdded(message.chat.id,message.text)
    setState(message.chat.id,"MainPage/")
    bot.mainMenu(message.chat.id)

@bot.bot.message_handler(func=pressedHistory)
def history(message):
    setState(message.chat.id,"MainPage/History")
    monthSum = 0
    messageInfo = ''
    for i in range(31):
        if getSumms(message.chat.id,i):

            monthSum += int(getSumms(message.chat.id,i))
            messageInfo+= "Ваши затраты <b>{}</b> числа этого месяца: <b>{}грн</b>.\n".format( i ,getSumms(message.chat.id, i))

    bot.print_message(message.chat.id,"{}В общем за месяц потрачено <b>{}</b>".format(messageInfo,monthSum))


    bot.mainMenu(message.chat.id)

if __name__ == "__main__":
    print("Hello World")

    bot.start_polling()