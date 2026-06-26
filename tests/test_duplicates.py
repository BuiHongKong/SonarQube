"""Test cho python/duplicate_a.py và duplicate_b.py - cover để sinh coverage."""

from python.duplicate_a import calculate_invoice
from python.duplicate_b import calculate_order

ITEMS = [
    {"price": 100, "quantity": 2},
    {"price": 50, "quantity": 12},
]


def test_calculate_invoice():
    result = calculate_invoice(ITEMS, 0.1, 0.08, "USD")
    assert result["currency"] == "USD"
    assert result["status"] in {"high_value", "medium_value", "low_value"}


def test_calculate_order():
    result = calculate_order(ITEMS, 0.1, 0.08, "USD")
    assert result["currency"] == "USD"
    assert result["status"] in {"high_value", "medium_value", "low_value"}


def test_invoice_and_order_match():
    a = calculate_invoice(ITEMS, 0.1, 0.08, "USD")
    b = calculate_order(ITEMS, 0.1, 0.08, "USD")
    assert a == b
