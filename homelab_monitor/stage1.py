def parse_line(line):
    split_line = line.strip().split()
    timestamp1 = str(split_line[0])
    try:
        splitted = timestamp1.split("-")
        if len(splitted) != 3:
            raise ValueError(f'Date not entered in correct format of YYYY-MM-DD. Recieved Value: ', {timestamp1})
    except:
        raise ValueError(f'An error occured verifying the date. Recieved Value: ', {timestamp1})
    timestamp2 = str(split_line[1])
    host = str(split_line[2])
    status = str(split_line[3])
    if status == "DOWN":
        latency = None
    else:
        latency = int(split_line[4])
    return {"timestamp": f'{timestamp1} {timestamp2}', "host": host, "status": status, "latency_ms": latency}