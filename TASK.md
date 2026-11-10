# Current task: Homelab Monitor, stage 1b - DOWN lines

A DOWN line has `-` where the latency would be:

```
2026-11-01 12:05:01 pihole DOWN -
```

`parse_line` must return `latency_ms` as `None` for these. Today `int("-")` crashes.

## Short lesson

Check the piece before you convert it:

```python
# a different problem
def parse_score(text):
    if text == "n/a":
        return None
    return int(text)

parse_score("42")    # 42
parse_score("n/a")   # None
```

`None` is Python's "no value". The check comes first, and the conversion only runs for pieces that really are numbers.

## Your task

Update `parse_line` in `homelab_monitor/stage1.py` so DOWN lines work. UP lines must keep working.

`tests/test_stage1b.py` is the spec. Don't edit it.

```
python -m pytest tests/test_stage1b.py
python -m pytest
```

When it passes, say "done" and I'll check your code.

## Coming up
- 1c: lines that don't fit the format (empty or garbage) raise `ValueError`
- 1d: `is_up` and `format_entry`
