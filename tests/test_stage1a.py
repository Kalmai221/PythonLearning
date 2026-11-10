from homelab_monitor.stage1 import parse_line


def test_parse_up_line():
    entry = parse_line("2026-11-01 12:00:01 nas-01 UP 12")
    assert entry == {
        "timestamp": "2026-11-01 12:00:01",
        "host": "nas-01",
        "status": "UP",
        "latency_ms": 12,
    }


def test_another_up_line():
    entry = parse_line("2026-11-01 12:15:01 plex UP 47")
    assert entry["host"] == "plex"
    assert entry["latency_ms"] == 47


def test_latency_is_an_int_not_a_string():
    entry = parse_line("2026-11-01 12:00:01 plex UP 45")
    assert isinstance(entry["latency_ms"], int)


def test_ignores_trailing_newline_and_spaces():
    entry = parse_line("2026-11-01 12:00:01 router UP 1  \n")
    assert entry["host"] == "router"
    assert entry["latency_ms"] == 1
