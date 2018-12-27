from config import shelve_name
import shelve
import datetime

#Функция добавления суммы для пользователя
def sumAdded(chat_id,sum):
    with shelve.open(shelve_name) as storage:
        now = datetime.datetime.now()
        try:
            answer = storage[str(chat_id)+" " +str(now.strftime("%d"))+" "+str(now.month)]
            storage[str(chat_id) + " " + str(now.strftime("%d")) + " " + str(now.month)] = str(int(answer) + int(sum))
        except KeyError:
            storage[str(chat_id) + " " + str(now.strftime("%d")) + " " + str(now.month)] = sum
        except ValueError:
            return None


#Получаем все затраты
def getSumms(chat_id,day):
    with shelve.open(shelve_name) as storage:
        now = datetime.datetime.now()
        try:
            answer = storage[str(chat_id) + " " + str(day) + " " + str(now.month)]
            return answer
        except KeyError:
            return None

#Состояние пользователя


def setState(chat_id,state):
    with shelve.open(shelve_name) as storage:
        storage[str(chat_id) + "State"] = state

def getState(chat_id):
    with shelve.open(shelve_name) as storage:
        try:
            answer = storage[str(chat_id) + "State"]
            return answer
        except KeyError:
            return None

#Удаление всех затрат за этот месяц
def dellInfo(chat_id):
    with shelve.open(shelve_name) as storage:

        now = datetime.datetime.now()
        for i in range(31):
            try:
                del storage[str(chat_id)+" "+str(i)+" "+str(now.month)]

            except KeyError:
                print("Miss + {}".format(i))