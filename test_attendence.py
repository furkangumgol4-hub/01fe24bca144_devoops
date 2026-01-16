from attendence import eligibility


def test_exact_75_percent():
    assert eligibility(100, 75) == 75.0


def test_above_75_percent():
    assert eligibility(80, 70) == 87.5


def test_below_75_percent():
    assert eligibility(60, 40) == (40 / 60) * 100


def test_full_attendance():
    assert eligibility(50, 50) == 100.0


def test_zero_attendance():
    assert eligibility(40, 0) == 0.0
