import pytest

from homelab_monitor.stage1 import parse_line


def test_empty_line_raises():
    with pytest.raises(ValueError):
        parse_line("")


def test_whitespace_only_raises():
    with pytest.raises(ValueError):
        parse_line("   \n")


def test_garbage_raises():
    with pytest.raises(ValueError):
        parse_line("this is not a log line")


def test_too_few_pieces_raises():
    with pytest.raises(ValueError):
        parse_line("2026-11-01 12:00:01 nas-01 UP")


def test_too_many_pieces_raises():
    with pytest.raises(ValueError):
        parse_line("2026-11-01 12:00:01 nas-01 UP 12 extra")


def test_unknown_status_raises():
    with pytest.raises(ValueError):
        parse_line("2026-11-01 12:00:01 nas-01 SIDEWAYS 12")


def test_up_with_dash_latency_raises():
    with pytest.raises(ValueError):
        parse_line("2026-11-01 12:00:01 nas-01 UP -")


def test_up_with_non_numeric_latency_raises():
    with pytest.raises(ValueError):
        parse_line("2026-11-01 12:00:01 nas-01 UP abc")


def test_down_with_a_number_raises():
    with pytest.raises(ValueError):
        parse_line("2026-11-01 12:00:01 nas-01 DOWN 12")


def test_error_message_is_not_empty():
    with pytest.raises(ValueError, match=r".+"):
        parse_line("")


def test_valid_lines_still_work():
    up = parse_line("2026-11-01 12:00:01 nas-01 UP 12")
    down = parse_line("2026-11-01 12:05:01 pihole DOWN -")
    assert up["latency_ms"] == 12
    assert down["latency_ms"] is None
