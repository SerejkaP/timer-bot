import time


def default_timer(text, hour, m, sec):
    ans = str(text)
    local_time = hour * 3600 + m * 60 + sec
    time.sleep(local_time)
    return ans

def for_sleeping(hour, m):
    hour -= 9
    if hour < 0:
        h = hour + 24
    else:
        h = hour
    local_time = h * 60 + m
    listTime = [i*90+local_time for i in range(6)]
    print(listTime)
    listHours = [listTime[i] // 60 for i in range(6)]
    print(listHours)
    listMinutes = [listTime[i] - listHours[i]*60 for i in range(6)]
    print(listMinutes)
    listSleeps = [str(listHours[i]) + ":" + str(listMinutes[i]) for i in range(6)]
    stringSleeps = ' '.join(listSleeps)
    return stringSleeps


