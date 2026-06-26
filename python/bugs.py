"""Các hàm đã được sửa đúng (đã làm sạch, không còn bug)."""


def check_status(code):
    if code == 200:
        return "OK"
    return "NOT OK"


def is_valid(a, b):
    return a is not None and b is not None


def compute(value):
    return value * 2


def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


def divide(a, b):
    if b == 0:
        return None
    return a / b


def always_true(x):
    if x not in (1, 2):
        return "luôn vào đây"
    return "không bao giờ"
