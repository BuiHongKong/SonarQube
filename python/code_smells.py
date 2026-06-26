"""Các hàm đã được làm sạch (không còn code smell)."""

CONNECTION_FAILED = "connection failed"
PREMIUM_THRESHOLD = 1000
PREMIUM_DISCOUNT = 0.9
STANDARD_DISCOUNT = 0.95

INCREMENT_BY_MODE = {"a": 1, "b": 4}
DEFAULT_INCREMENT = 5


def process(data, mode):
    increment = INCREMENT_BY_MODE.get(mode, DEFAULT_INCREMENT)
    return len(data) * increment


def risky():
    try:
        return int("not-a-number")
    except ValueError:
        return None


def magic_numbers(price):
    if price > PREMIUM_THRESHOLD:
        return price * PREMIUM_DISCOUNT
    return price * STANDARD_DISCOUNT


def repeated_literals():
    return CONNECTION_FAILED


def unused_variables():
    return 42
