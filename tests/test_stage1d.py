import pytest

from homelab_monitor.stage1 import format_entry, is_up, parse_line


# --- parse_line: cleanup checks ------------------------------------------

def test_bad_date_raises():
    with pytest.raises(ValueError):
        parse_line("abc 12:00:01 nas UP 5")


def test_bad_time_raises():
    with pytest.raises(ValueError):
        parse_line("2026-11-01 xyz nas UP 5")


def test_time_missing_seconds_raises():
    with pytest.raises(ValueError):
        parse_line("2026-11-01 12:00 nas UP 5")


def test_negative_latency_raises():
    with pytest.raises(ValueError):
        parse_line("2026-11-01 12:00:01 nas UP -5")


def test_error_message_contains_the_bad_line():
    with pytest.raises(ValueError, match="garbage"):
        parse_line("garbage")


def test_valid_lines_still_parse():
    entry = parse_line("2026-11-01 12:00:01 nas-01 UP 12")
    assert entry["timestamp"] == "2026-11-01 12:00:01"
    assert entry["latency_ms"] == 12


def test_stretch_month_13_raises():
    with pytest.raises(ValueError):
        parse_line("2026-13-01 12:00:01 nas UP 5")


# --- is_up ---------------------------------------------------------------

def test_is_up_true():
    assert is_up({"status": "UP"}) is True


def test_is_up_false():
    assert is_up({"status": "DOWN"}) is False


# --- format_entry --------------------------------------------------------

def test_format_up():
    entry = {"timestamp": "t", "host": "nas-01", "status": "UP", "latency_ms": 12}
    assert format_entry(entry) == "nas-01 is UP (12 ms)"


def test_format_down():
    entry = {"timestamp": "t", "host": "pihole", "status": "DOWN", "latency_ms": None}
    assert format_entry(entry) == "pihole is DOWN"


def test_format_roundtrip_from_a_real_line():
    entry = parse_line("2026-11-01 12:05:01 pihole DOWN -")
    assert format_entry(entry) == "pihole is DOWN"
