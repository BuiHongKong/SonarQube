"""Test cho python/billing.py - cover đủ các nhánh status."""

from python.billing import summarize_billing


def test_high_value():
    items = [{"price": 1000, "quantity": 5}]
    result = summarize_billing(items, 0.0, 0.0, "USD")
    assert result["status"] == "high_value"


def test_medium_value():
    items = [{"price": 100, "quantity": 5}]
    result = summarize_billing(items, 0.0, 0.0, "USD")
    assert result["status"] == "medium_value"


def test_low_value():
    items = [{"price": 10, "quantity": 1}]
    result = summarize_billing(items, 0.0, 0.0, "USD")
    assert result["status"] == "low_value"


def test_bulk_discount_applied():
    items = [{"price": 10, "quantity": 20}]
    result = summarize_billing(items, 0.0, 0.0, "USD")
    # 10 * 20 * 0.95 = 190
    assert result["subtotal"] == 190.0
