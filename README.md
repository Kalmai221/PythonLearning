# Relearning Python

I got too reliant on AI to write my code, and my own Python skills went rusty. This repo is how I'm fixing that: relearning Python from the ground up, in public, by writing the code myself.

## Why this repo exists

AI is very good at producing working code. That is exactly the problem: if it writes everything, I stop learning how to write anything. I want to be able to read, write and debug Python on my own.

## How it works

I use an AI assistant (Claude) as a **mentor, not a code writer**. The rules are in [`CLAUDE.md`](CLAUDE.md):

- It never writes my solution code. I write every function in `homelab_monitor/`.
- It writes the **tests** (`tests/`) and the lesson notes, and reviews my code.
- When I'm stuck I get hints in tiers: a question, a concept to look up, an outline, then a similar example. Never the answer.
- I only move on when the tests pass and the review shows I understand it.
- My level, attempts and the concepts I got wrong are logged honestly in [`PROGRESS.md`](PROGRESS.md), including the mistakes.

So the tests and lesson text here are AI-written, and the solutions are mine. That split is the whole point.

## The projects

| Project | What it is | Status |
|---------|------------|--------|
| 0. Status Board | Four small functions on host statuses | Done |
| 1. Homelab Monitor | Reads uptime logs from my homelab services and reports what's up, down and slow | In progress (stage 1) |

Homelab Monitor grows over ten stages: parsing, data structures, file I/O, classes, network checks, APIs, concurrency, testing, architecture, and performance. The full plan is in [`ROADMAP.md`](ROADMAP.md).

## Log format

```
2026-11-01 12:00:01 nas-01 UP 12
2026-11-01 12:05:01 pihole DOWN -
```

`date time host status latency_ms` (`-` when the host is down). Sample data is in `data/sample.log`.

## Repo layout

```
homelab_monitor/   my code (starter.py, stage1.py, ...)
tests/             tests, one file per step
data/              sample logs
CLAUDE.md          the mentor rules
PROGRESS.md        level log and mistakes
ROADMAP.md         the plan
TASK.md            the current task
```

## Running the tests

Requires Python 3.10+.

```
pip install -r requirements-dev.txt
python -m pytest
```

Tests for steps I haven't reached yet will fail or fail to import. That's expected.
