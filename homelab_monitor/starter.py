def is_up(status):
    if status.upper() == "UP":
        return True
    else:
        return False

def label(host, status):
    return f'{host}: {status.upper()}'

def speed(ms):
    ms = int(ms)
    if ms < 50:
        return "fast"
    elif (ms >= 50) and (ms <=199):
        return "ok"
    else:
        return "slow"

def count_up(statuses):
    count = 0
    for x in statuses:
        if x.upper() == "UP":
            count = count + 1
    return count