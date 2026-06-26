"""Logic tính tiền dùng chung để tránh trùng lặp code."""

LOW_VALUE_THRESHOLD = 100
HIGH_VALUE_THRESHOLD = 1000
BULK_QUANTITY = 10
BULK_DISCOUNT = 0.95


def summarize_billing(items, discount_rate, tax_rate, currency):
    subtotal = 0
    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 1)
        line_total = price * quantity
        if quantity > BULK_QUANTITY:
            line_total *= BULK_DISCOUNT
        subtotal += line_total

    discount = subtotal * discount_rate
    taxable = subtotal - discount
    tax = taxable * tax_rate
    total = taxable + tax

    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "tax": round(tax, 2),
        "total": round(total, 2),
        "currency": currency,
        "status": _status_for(total),
    }


def _status_for(total):
    if total > HIGH_VALUE_THRESHOLD:
        return "high_value"
    if total > LOW_VALUE_THRESHOLD:
        return "medium_value"
    return "low_value"
