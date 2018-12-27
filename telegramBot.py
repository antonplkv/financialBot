import telebot
from telebot import types

class MoneyBot:
    def __init__(self,token):
        self.bot = telebot.TeleBot(token)

    def print_message(self, message_id, message_text):
        """
        Функция отправляет сообщение пользователю без клавиатуры
        :param message_id: Идентификатор пользователя
        :param message_text: Текст сообщения
        :return: Функция ничего не возвращает
        """
        self.bot.send_message(message_id, message_text, reply_markup=types.ReplyKeyboardRemove(),parse_mode="HTML")

    #generation of common keyboard
    def get_keyboard(self,keyboard_tuple_list):
        message_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for i in range(0, len(keyboard_tuple_list)):
            message_keyboard.row(*keyboard_tuple_list[i])
        return message_keyboard

    #generation of inline keyboard
    def get_inline_keyboard(self,keyboard_tuple_list):
        message_keyboard = types.InlineKeyboardMarkup()
        for i in range(0, len(keyboard_tuple_list)):
            message_keyboard.row(*keyboard_tuple_list[i])
        return message_keyboard

    def start_polling(self):
        """
        Функция начинает опрос бота методом polling
        :return:Функция ничего не возвращает
        """
        self.bot.polling(none_stop=True)

    def print_keyboard_message(self, message_id, message_text, message_keyboard):
        """
        Функция отправляет сообщение пользователю с клавиатурой
        :param message_id: Идентификатор пользователя
        :param message_text:  Текст сообщения
        :param message_keyboard: Клавиатура типа ReplyKeyboardMarkup
        :return: Функция ничего не возвращает
        """
        self.bot.send_message(message_id, message_text, reply_markup=message_keyboard)

    def print_picture(self, message_id, photo_url):
        self.bot.send_photo(message_id, photo_url)

    def print_keyboard_picture(self, message_id, photo_url, message_keyboard):
        self.bot.send_photo(message_id, photo_url, reply_markup=message_keyboard)

    def update_message_text(self, chat_id, message_id, message_text, message_keyboard):
        self.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text,
                                   reply_markup=message_keyboard)

    def update_message_text_html(self, chat_id, message_id, message_text, message_keyboard):
        self.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text,
                                   reply_markup=message_keyboard, parse_mode='HTML')

    def print_keyboard_message_html(self, message_id, message_text, message_keyboard):
        self.bot.send_message(message_id, message_text, reply_markup=message_keyboard, parse_mode='HTML')

    def keyboard_tuple(self,keyboard_list, count):
        """
        Функция генерирует tuple для клавиатуры из списка
        :param keyboard_list: список кнопок
        :param count: количество кнопок в строке
        :return: Список tuple.
        """
        tuple_list = []
        row = ()
        for i in range(0, len(keyboard_list)):
            if i > 0 and i % count == 0:
                tuple_list.append(row)
                row = (keyboard_list[i],)
            else:
                row += (keyboard_list[i],)
        if row != ():
            tuple_list.append(row)
        return tuple_list

    def mainMenu(self,id):
        button = ("Потратил бабки :(", "История бабла", "Главная")
        keyboard = self.get_keyboard(self.keyboard_tuple(button, 1))
        self.print_keyboard_message_html(id,
                                        "Выбери пункт меню!", keyboard)
