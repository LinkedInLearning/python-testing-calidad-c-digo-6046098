import pytest

from divide import divide


def test_divide():
    assert divide(10, 5) == 2.0


def test_zero_division():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "Unable to divide by zero" in str(excinfo.value)


def test_divide_negative_number():
    assert divide(-10, 2) == -5.0
