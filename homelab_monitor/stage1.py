def parse_line(line):
    split_line = line.strip().split()
    if len(split_line) != 5:
        raise ValueError("Invalid data provided.")
    try:
        timestamp1 = str(split_line[0])
        splitted = timestamp1.split("-")
        if len(splitted) == 3:
            worked = True
    except:
        raise ValueError(f'An error occured verifying the date. Recieved Value: ', {str(split_line[0])})
    finally:
        try:
            timestamp2 = str(split_line[1])
            splitted = timestamp2.split(":")
            if len(splitted) == 3:
                worked = True
        except:
            raise ValueError(f'An error occured verifying the time. Recieved Value: ', {str(split_line[1])})
        finally:
            try:
                host = str(split_line[2])
                if host != "":
                    worked = True
            except:
                raise ValueError("No Host has been provided")
            finally:
                status = str(split_line[3])
                latency = split_line[4]
                if status == "DOWN":
                    if latency == "-":
                        latency = None
                    else:
                        raise ValueError("Latency Provided when Host Status is DOWN")
                elif status == "UP":
                    latency = int(split_line[4])
                else:
                    raise ValueError("Invalid status has been provided.")
                worked = True
    if worked:    
        return {"timestamp": f'{timestamp1} {timestamp2}', "host": host, "status": status, "latency_ms": latency}