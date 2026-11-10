from homelab_monitor.starter import count_up, is_up, label, speed


# --- step 1 -------------------------------------------------------------

def test_is_up_true():
    assert is_up("UP") is True


def test_is_up_false():
    assert is_up("DOWN") is False


# --- step 2 -------------------------------------------------------------

def test_label():
    assert label("nas-01", "UP") == "nas-01: UP"
    assert label("pihole", "DOWN") == "pihole: DOWN"


# --- step 3 -------------------------------------------------------------

def test_speed_fast():
    assert speed(3) == "fast"
    assert speed(49) == "fast"


def test_speed_ok():
    assert speed(50) == "ok"
    assert speed(199) == "ok"


def test_speed_slow():
    assert speed(200) == "slow"
    assert speed(900) == "slow"


# --- step 4 -------------------------------------------------------------

def test_count_up():
    assert count_up(["UP", "DOWN", "UP", "UP"]) == 3


def test_count_up_none_up():
    assert count_up(["DOWN", "DOWN"]) == 0


def test_count_up_empty():
    assert count_up([]) == 0
