"""Test cho python/bugs.py - cover các hàm thuần để sinh coverage."""

from python.bugs import (
    always_true,
    append_item,
    check_status,
    compute,
    divide,
    is_valid,
)


def test_check_status_ok():
    assert check_status(200) == "OK"


def test_check_status_not_ok():
    assert check_status(404) == "NOT OK"


def test_is_valid():
    assert is_valid(1, 2) is True


def test_compute():
    assert compute(3) == 6


def test_append_item():
    assert append_item(1, []) == [1]


def test_divide():
    assert divide(10, 2) == 5.0


def test_always_true():
    assert always_true(5) == "luôn vào đây"
