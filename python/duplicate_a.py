"""Demo Duplications - file A. Khối logic bên dưới gần như giống hệt duplicate_b.py."""


def calculate_invoice(items, discount_rate, tax_rate, currency):
    subtotal = 0
    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 1)
        line_total = price * quantity
        if quantity > 10:
            line_total = line_total * 0.95
        subtotal += line_total

    discount = subtotal * discount_rate
    taxable = subtotal - discount
    tax = taxable * tax_rate
    total = taxable + tax

    summary = {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "tax": round(tax, 2),
        "total": round(total, 2),
        "currency": currency,
    }

    if total > 1000:
        summary["status"] = "high_value"
    elif total > 100:
        summary["status"] = "medium_value"
    else:
        summary["status"] = "low_value"

    return summary
