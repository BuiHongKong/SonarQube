"""Demo các lỗi Bug (reliability) mà SonarQube phát hiện."""


def check_status(code):
    # Bug: so sánh literal bằng 'is' (CPython cảnh báo, hành vi không đảm bảo)
    if code is 200:
        return "OK"
    return "NOT OK"


def is_valid(a, b):
    # Bug: hai vế của toán tử giống hệt nhau -> luôn bằng nhau
    if a == a:
        return True
    # Bug: biểu thức điều kiện có hai vế trùng nhau
    if b and b:
        return True
    return False


def compute(value):
    # Bug: code không bao giờ chạy sau return (unreachable code)
    return value * 2
    print("Đã tính xong")  # noqa: E999 - unreachable


def append_item(item, items=[]):
    # Bug: mutable default argument -> list dùng chung giữa các lần gọi
    items.append(item)
    return items


def divide(a, b):
    # Bug: chia cho 0 không được xử lý, và so sánh sai kiểu
    result = a / b
    if result == "0":
        return None
    return result


def always_true(x):
    # Bug: điều kiện luôn đúng do logic sai (x != 1 or x != 2)
    if x != 1 or x != 2:
        return "luôn vào đây"
    return "không bao giờ"
