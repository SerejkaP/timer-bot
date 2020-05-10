import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# API токен сообщества
mytoken = '93d891c18343c9467352320cbc4507acda2803b120a4324535bf31ac9e16a1ab403b0444027508157e26e'


# Функция посылающая сообщение
def write_msg(user_id, message):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})


# Авторизуемся как сообщество
vk = vk_api.VkApi(token=mytoken)
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Логика формирования ответа бота
            if ('Старт' in request):
                answer = 'Ну, я пока не знаю, что начинать('
            else:
                answer = 'Если Вы хотите начать, напишите мне "Старт"'

            write_msg(event.user_id, answer)