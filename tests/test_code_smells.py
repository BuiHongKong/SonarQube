"""Test cho python/code_smells.py - cover các hàm thuần để sinh coverage."""

from python.code_smells import (
    magic_numbers,
    process,
    repeated_literals,
    risky,
    unused_variables,
)


def test_magic_numbers_high():
    assert magic_numbers(2000) == 1800.0


def test_magic_numbers_low():
    assert magic_numbers(500) == 475.0


def test_repeated_literals():
    assert repeated_literals() == "connection failed"


def test_unused_variables():
    assert unused_variables() == 42


def test_risky_returns_none():
    assert risky() is None


def test_process_mode_a():
    assert process([1, 2, 3], "a") == 3


def test_process_mode_b():
    assert process([1], "b") == 4


def test_process_default():
    assert process([1], "c") == 5
