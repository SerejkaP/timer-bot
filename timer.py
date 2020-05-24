import time


# Таймер
def default_timer(text, hour, m, sec):
    ans = str(text)
    local_time = hour * 3600 + m * 60 + sec
    time.sleep(local_time)
    return ans


# Калькулятор для времени сна
def for_sleeping(hour, m):
    hour -= 9
    if hour < 0:
        h = hour + 24
    else:
        h = hour
    local_time = h * 60 + m  # Перевод времени в минуты
    listTime = [i * 90 + local_time for i in range(6)]  # Заполнение массива с периодами в полтора часа
    print(listTime)
    first_listHours = [listTime[i] // 60 for i in range(6)]  # Подсчёт часов
    print(first_listHours)
    listMinutes = [listTime[i] - first_listHours[i] * 60 for i in range(6)]  # Подсчёт минут
    for i in range(6):
        if listMinutes[i] == 0:
            listMinutes[i] = "00"
    print(listMinutes)
    second_listHours = first_listHours
    for i in range(6):
        if first_listHours[i] > 23:
            first_listHours[i] -= 24
        if first_listHours[i] == 0:
            first_listHours[i] = "00"
    listSleeps = [str(second_listHours[i]) + ":" + str(listMinutes[i]) for i in
                  range(6)]  # Заполнение списка отформатированным временем
    stringSleeps = ' '.join(listSleeps)
    print(first_listHours)
    return stringSleeps


# Проверка записи на правильность
def checker(arg, function_type):
    arrMsg = str(arg).split()
    chk = 0
    if function_type == 0:  # Для обычного таймера
        if len(arrMsg) == 3 and len(arrMsg[2].split(':')) == 3:
            return
        else:
            print("ERROR")
            return chk
    if function_type == 1:  # Для таймера с циклами
        if len(arrMsg) == 4 and len(arrMsg[2].split(':')) == 3:
            return
        else:
            print("ERROR")
            return chk
    if function_type == 2:  # Для калькулятора сна
        if len(arrMsg) == 2 and len(arrMsg[1].split(':')) == 2:
            return
        else:
            print("ERROR")
            return chk
