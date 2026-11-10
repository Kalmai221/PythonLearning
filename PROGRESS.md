# PROGRESS

**Current project:** 0 - Status Board (starter)
**Started:** 2026-11-10 (full restart, then shrunk again)
**Limit found so far:** Homelab Monitor stage 1 (parse a log line) was too big a first step.

## Background
- Self-reported: knows some Python, rusty after relying on AI.
- Earlier calibration (2026-11-01): list aliasing and mutable default arguments answered correctly (no explanation given yet); `d[key]` vs `d.get(key)` unknown; counting into a dict unknown.
- Large first tasks stalled, so everything starts with a REPL warm-up and tiny steps.

## Rules of advancement
- Clear a step only when tests pass AND I explain the code in my own words.
- Pass easily -> skip ahead. Fail twice -> stay and teach.

## Log

| Date | Project / step | Task | Attempts | Hint tier used | Concepts fumbled | Explained in own words? | Result |
|------|----------------|------|----------|----------------|------------------|-------------------------|--------|
| 2026-11-10 | 0 / step 0 | REPL warm-up | 0 | - | - | - | assigned |
| 2026-11-10 | 0 / 1-4 | is_up, label, speed, count_up | 1 | - | Function name mismatch (`isup` vs `is_up`); unrequested `.upper()`/`int()` added as an uneven safety net; redundant `ms >= 50`; believes `elif` conditions must restate earlier bounds | Attempt 1: no. Traced speed(120) through the `else` branch (does not know `return` exits the function). Thought an indented `return` in a loop is an error (it is valid, but returns on the first iteration). | tests pass, step NOT cleared |

| 2026-11-10 | 0 | Status Board | - | - | `return` ends a function; `return` inside a loop is valid but exits on first pass | Waived at user request | CLEARED (tests pass; concept to revisit) |
| 2026-11-10 | 1 / 1a | parse_line (UP lines) | 2 | 3 (outline) | Used `global` state; mixed up dict key/value; looped over data that did not line up with names; redundant `str()` | n/a | CLEARED (4 tests pass) |
| 2026-11-10 | 1 / 1b | parse_line (DOWN lines) | 1 | - | Keyed on status instead of the `-` itself (`UP -` crashes, `DOWN 12` silently drops data); redundant `str()` and numbered names left in after review | n/a | CLEARED (17 tests pass) |
| 2026-11-10 | 1 / 1c | parse_line (bad lines raise ValueError) | 0 | - | - | n/a | assigned |

## Preferences
- 2026-11-10: User does not want to be quizzed. Workflow is: short lesson, coding task, review of code. No explanation gate.

## Sessions
- 2026-11-10: Restarted with Homelab Monitor, which was too big. Added Project 0 (Status Board) as an easier first project. Stage 1 tests parked in tests/_parked/.
