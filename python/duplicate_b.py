"""Tính đơn hàng - delegate sang billing dùng chung (đã gỡ trùng lặp)."""

from python.billing import summarize_billing


def calculate_order(items, discount_rate, tax_rate, currency):
    return summarize_billing(items, discount_rate, tax_rate, currency)
