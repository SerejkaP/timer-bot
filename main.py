import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import timer

# команды
bot_commands = ["СТАРТ", "КОНЕЦ", "ПОМОЩЬ", "ЦИКЛ", "ТАЙМЕР:", "ЦИКЛ:", "СОН", "СОН:"]

# Токен
file = open('token.TXT', 'r')
mytoken = file.read()


# Функция посылающая сообщение
def write_msg(user_id, message):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})


# Авторизуемся как сообщество
vk = vk_api.VkApi(token=mytoken)
longpoll = VkLongPoll(vk)


def heartbreaker(arg):
    arrMsg = arg.split()
    return arrMsg, len(arrMsg)


# Основной цикл
def new_message():
    for event in longpoll.listen():
        # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            # Если оно имеет метку для бота
            if event.to_me:
                # Сообщение от пользователя
                request = event.text
                # Обработка сообщения
                arrMsg, length = heartbreaker(request)
                # Ответ на команды ботом
                if arrMsg[0].upper() == bot_commands[0]:  # Текст для таймера
                    msg = f"Для запуска таймера напишите 'таймер:', что напомнить и время через двоеточие. (Пример:'таймер: слово 3:2:2') "
                elif arrMsg[0].upper() == bot_commands[1]:  # Прощание
                    msg = "До свидания!"
                elif arrMsg[0].upper() == bot_commands[2]:  # Помощь по командам
                    msg = f'Список команд: "СТАРТ", "КОНЕЦ", "ПОМОЩЬ", "ЦИКЛ", "СОН"'
                elif arrMsg[0].upper() == bot_commands[3]:  # Текст для таймера-цикла
                    msg = f"Для запуска таймера  сциклом напишите 'цикл:', что напомнить, время через двоеточие и " \
                          f"количество циклов. (Цикл:'таймер: слово 3:2:2 5') "
                elif arrMsg[0].upper() == bot_commands[4]:  # Таймер
                    if timer.checker(request, 0) == 0:
                        msg = f"Неверная запись"
                    else:
                        argTime = arrMsg[2].split(':')
                        msg = timer.default_timer(arrMsg[1], int(argTime[0]), int(argTime[1]), int(argTime[2]))
                elif arrMsg[0].upper() == bot_commands[5]:  # Таймер с циклами
                    if timer.checker(request, 1) == 0:
                        msg = f"Неверная запись"
                    else:
                        argTime = arrMsg[2].split(':')
                        num = int(arrMsg[3])
                        while num > 1:
                            msg = timer.default_timer(arrMsg[1], int(argTime[0]), int(argTime[1]), int(argTime[2]))
                            write_msg(event.user_id, msg)
                            num -= 1
                elif arrMsg[0].upper() == bot_commands[6]:  # Текст для подборки времени сна
                    msg = f"Введите время, когда хотите проснуться, и я подсчитаю, когда лучше лечь спать. Человеку " \
                          f"нужно 14 минут в среднем, чтобы уснуть... (Пример записи: 'Сон: 23:00') "
                elif arrMsg[0].upper() == bot_commands[7]:  # Подбор времени сна
                    if timer.checker(request, 2) == 0:
                        msg = f"Неверная запись"
                    else:
                        argTime = arrMsg[1].split(':')
                        time_for_sleep = ''.join(timer.for_sleeping(int(argTime[0]), int(argTime[1])).split(','))
                        msg = "Время, когда лучше уснуть: " + time_for_sleep
                else:  # Приветственное сообшение
                    msg = f"Здравствуйте! Если Вам нужен список команд, напишите 'помощь'"
                write_msg(event.user_id, msg)


def main():
    new_message()


if __name__ == '__main__':
    main()
