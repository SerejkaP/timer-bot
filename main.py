import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import timer

# команды
bot_commands = ["СТАРТ", "КОНЕЦ", "ПОМОЩЬ", "ЦИКЛ", "ТАЙМЕР:", "ЦИКЛ:", "СОН", "СОН:"]

global boolTimer

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

def checker(arg):
    arrMsg=arg.split()
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
                arrMsg, length = checker(request)
                # Ответ на команды ботом
                if arrMsg[0].upper() == bot_commands[0]:
                    msg = f"Для запуска таймера напишите 'таймер:', что напомнить и время через двоеточие. (Пример:'таймер: слово 3:2:2')"
                elif arrMsg[0].upper() == bot_commands[1]:
                    msg = "До свидания!"
                elif arrMsg[0].upper() == bot_commands[2]:
                    msg = f"Список команд: 'СТАРТ', 'КОНЕЦ', 'ЗАПУСК', 'ПОМОЩЬ','СТОП', 'СОН', 'ЦИКЛ'"
                elif arrMsg[0].upper() == bot_commands[3]:
                    msg = f"Для запуска таймера  сциклом напишите 'цикл:', что напомнить, время через двоеточие и количество циклов. (Цикл:'таймер: слово 3:2:2 5')"
                elif arrMsg[0].upper() == bot_commands[4]:
                    argTime = arrMsg[2].split(':')
                    msg = timer.default_timer(arrMsg[1], int(argTime[0]), int(argTime[1]), int(argTime[2]))
                elif arrMsg[0].upper() == bot_commands[5]:
                    argTime = arrMsg[2].split(':')
                    num = int(arrMsg[3])
                    while num > 1:
                        msg = timer.default_timer(arrMsg[1], int(argTime[0]), int(argTime[1]), int(argTime[2]))
                        write_msg(event.user_id, msg)
                        num -= 1
                elif arrMsg[0].upper() == bot_commands[6]:
                    msg = f"Введите время, когда хотите проснуться. Человеку нужно 14 минут в среднем, чтобы уснуть... (Пример записи: 'Сон: 23:00')"
                elif arrMsg[0].upper() == bot_commands[7]:
                    argTime = arrMsg[1].split(':')
                    msg = "Время, когда лучше уснуть:"
                else:
                    msg = f"Здравствуйте! Если Вам нужен список команд, напишите 'помощь'"
                write_msg(event.user_id, msg)

def main():
    new_message()

if __name__ == '__main__':
    main()