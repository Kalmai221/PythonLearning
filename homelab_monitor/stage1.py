def parse_line(line):
    split_line = line.strip().split()
    timestamp1 = str(split_line[0])
    timestamp2 = str(split_line[1])
    host = str(split_line[2])
    status = str(split_line[3])
    latency = int(split_line[4])
    return {"timestamp": f'{timestamp1} {timestamp2}', "host": host, "status": status, "latency_ms": latency}