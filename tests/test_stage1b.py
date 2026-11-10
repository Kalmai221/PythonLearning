from homelab_monitor.stage1 import parse_line


def test_parse_down_line():
    entry = parse_line("2026-11-01 12:05:01 pihole DOWN -")
    assert entry == {
        "timestamp": "2026-11-01 12:05:01",
        "host": "pihole",
        "status": "DOWN",
        "latency_ms": None,
    }


def test_down_latency_is_none_not_a_string():
    entry = parse_line("2026-11-01 12:10:01 nas-01 DOWN -")
    assert entry["latency_ms"] is None


def test_down_with_trailing_newline():
    entry = parse_line("2026-11-01 12:10:01 nas-01 DOWN -\n")
    assert entry["status"] == "DOWN"
    assert entry["latency_ms"] is None


def test_up_lines_still_work():
    entry = parse_line("2026-11-01 12:00:01 nas-01 UP 12")
    assert entry["status"] == "UP"
    assert entry["latency_ms"] == 12
