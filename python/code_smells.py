"""Demo các lỗi Code Smell (maintainability) mà SonarQube phát hiện."""

import json  # unused import
import math  # unused import


def process(data, mode, level, retry, verbose, flag):
    # Code smell: quá nhiều tham số + cognitive complexity cao (lồng nhiều if/for)
    result = 0
    for i in range(len(data)):
        if mode == "a":
            if level > 1:
                if retry:
                    if verbose:
                        for j in range(i):
                            if flag:
                                result += i * j
                            else:
                                result -= j
                    else:
                        result += 1
                else:
                    result += 2
            else:
                result += 3
        elif mode == "b":
            if level > 5:
                result *= 2
            else:
                result += 4
        else:
            result += 5
    return result


def risky():
    try:
        return 10 / 0
    except:  # noqa: E722 - empty except nuốt exception
        pass


def magic_numbers(price):
    # Code smell: magic numbers
    if price > 1000:
        return price * 0.9
    return price * 0.95


def repeated_literals():
    # Code smell: chuỗi lặp lại nhiều lần (duplicate string literal)
    log("connection failed")
    log("connection failed")
    log("connection failed")
    save("connection failed")
    return "connection failed"


def unused_variables():
    # Code smell: biến không được sử dụng
    total = 100
    name = "demo"
    temp = total + 1
    return 42


# Code smell: code bị comment lại (commented-out code)
# def old_function(x):
#     return x + 1
#     y = x * 2

# TODO: refactor module này


def log(message):
    print(message)


def save(message):
    print("saved:", message)
