import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

bot_commands = ["СТАРТ", "КОНЕЦ", "ЗАПУСК", "ПОМОЩЬ"] #команды

file = open('token.TXT', 'r') #токен
mytoken = file.read()

# Функция посылающая сообщение
def write_msg(user_id, message):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=mytoken)
longpoll = VkLongPoll(vk)

#Выбор команды для бота
def new_message(message):
    if message.upper() == bot_commands[0]:
        return f"Здравствуйте! Если Вам нужен список команд, напишите 'помощь'"
    elif message.upper() == bot_commands[1]:
        return f"До свидания!"
    elif message.upper() == bot_commands[2]:
        return f"Здесь будет запуск таймера"
    elif message.upper() == bot_commands[3]:
        return f"Список команд: 'СТАРТ', 'КОНЕЦ', 'ЗАПУСК', 'ПОМОЩЬ'"
    else:
        return f"Напишите 'Старт'"

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text
            write_msg(event.user_id, new_message(request))