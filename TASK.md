# Current task: Homelab Monitor, stage 1d - cleanup, `is_up`, `format_entry`

## 1. Clean up `parse_line`
Your tests pass, but these slip through today:

```
'abc 12:00:01 nas UP 5'            -> accepted (should raise)
'2026-11-01 xyz nas UP 5'          -> accepted (should raise)
'2026-11-01 12:00:01 nas UP -5'    -> accepted (should raise)
```

- Delete the `try` / `except` / `finally` structure and the `worked` flag. Line 3 already guarantees five pieces, so nothing in them can fail.
- Make the date and time checks **raise** when they fail. Right now they only do something when they succeed.
- Reject negative latency.
- Put the bad line in the error message (`{line!r}`), so the error says what was wrong.
- Drop the `str()` calls on pieces that are already strings.

## 2. `is_up(entry)`
Returns `True` if the entry's status is `"UP"`, otherwise `False`. `entry` is the dict `parse_line` returns.

## 3. `format_entry(entry)`
- `"nas-01 is UP (12 ms)"` for an UP entry
- `"pihole is DOWN"` when latency is `None`

## Short lesson
```python
# a different problem
def describe(entry):                      # entry = {"name": "Sam", "score": None}
    if entry["score"] is None:
        return f'{entry["name"]} has no score'
    return f'{entry["name"]} scored {entry["score"]}'
```
- Read a dict value with `entry["key"]`.
- Test for missing data with `is None`.
- Inside an f-string, use a **different** quote type for the keys than for the string itself.

## Stretch (optional)
`test_stretch_month_13_raises` needs real date validation. Look up `datetime.strptime`. Everything else works without it.

## Run the tests
```
python -m pytest tests/test_stage1d.py
python -m pytest
```

`tests/test_stage1d.py` is the spec. Don't edit it. Say "done" when it passes.

## After this
Stage 1 is finished. Stage 2: summarising many log lines at once (uptime per host, slowest host, outages) with lists, dicts and loops.
