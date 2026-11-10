# Roadmap

Two projects. Each stage is harder than the last. Each stage has tests (mine) and code (yours).

**Gate for every stage:** all tests pass AND you explain your code in your own words.
The stage where you fail twice is your current limit. We log it and teach it.

## Project 0: Status Board (start here)
Four tiny functions on a single host status.

| Step | You build | You practise |
|------|-----------|--------------|
| 1 | `is_up(status)` | functions, `return`, `==` |
| 2 | `label(host, status)` | strings, f-strings |
| 3 | `speed(ms)` | `if` / `elif` / `else`, edge values |
| 4 | `count_up(statuses)` | lists, `for` loops, counting |

## Project 1: Homelab Monitor

| Stage | Level | You build | You practise |
|-------|-------|-----------|--------------|
| 1 | Fundamentals | Parse one log line into a dict | strings, `int()`, dicts, `raise` |
| 2 | Data structures | Summarise many entries | lists, dicts, sorting, comprehensions |
| 3 | File I/O | Read a log file, write a report | `with open`, `pathlib`, JSON/CSV |
| 4 | OOP | `Host` and `Check` classes | classes, `__init__`, dataclasses |
| 5 | Network I/O | Real TCP and HTTP checks | `socket`, `urllib`/`requests`, timeouts |
| 6 | APIs and config | Config file, webhook alerts | JSON/YAML, REST |
| 7 | Concurrency | Check many hosts at once | threads, `asyncio` |
| 8 | Testing | Test network code offline | fixtures, mocks, parametrize |
| 9 | Architecture | Package with CLI and logging | `argparse`, `logging` |
| 10 | Performance | Handle a 1 GB log | generators, profiling |

Project 0 is cleared. Stage 1 is split into small steps (1a, 1b, ...), each with its own tests.

## Folder layout
```
homelab_monitor/   your code (starter.py, stage1.py, ...)
tests/             my tests (don't edit)
data/              sample logs and config
```
