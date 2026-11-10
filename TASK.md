# Current task: Homelab Monitor, stage 1c - bad lines raise ValueError

Real logs contain junk: empty lines, half-written lines, corrupted lines. Right now `parse_line("")` crashes with `IndexError`, which says nothing useful. Check the line first, and raise a clear error yourself.

## Short lesson

```python
# different problems
def parse_pair(text):
    parts = text.split()
    if len(parts) != 2:
        raise ValueError(f"expected 2 parts, got {len(parts)}: {text!r}")
    return parts

def pick_colour(name):
    if name not in ("red", "green", "blue"):
        raise ValueError(f"unknown colour: {name!r}")
    return name
```

- `raise ValueError("message")` stops the function immediately and reports the problem.
- `len(parts)` counts the pieces.
- `x in (a, b, c)` checks whether `x` is one of several allowed values.
- `raise` stops the function, so the check goes **before** the code that would crash.

## Your task

Update `parse_line` in `homelab_monitor/stage1.py` so it raises `ValueError` when:
- the line is empty or has the wrong number of pieces,
- the status is not `UP` or `DOWN`,
- an `UP` line has no number for latency (`UP -`, `UP abc`),
- a `DOWN` line has anything but `-` for latency (`DOWN 12`).

Valid lines behave exactly as before. Also use a helpful error message (it must not be empty).

`tests/test_stage1c.py` is the spec. Don't edit it.

```
python -m pytest tests/test_stage1c.py
python -m pytest
```

When it passes, say "done" and I'll check your code.

## Also
Clean up the `str()` calls and the `timestamp1`/`timestamp2` names while you are in there.

## Coming up
- 1d: `is_up` and `format_entry`. That finishes stage 1.
- Stage 2: summarising many entries at once.
