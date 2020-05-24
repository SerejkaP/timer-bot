import time


def default_timer(text, hour, m, sec):
    ans = str(text)
    local_time = hour * 3600 + m * 60 + sec
    time.sleep(local_time)
    return ans



