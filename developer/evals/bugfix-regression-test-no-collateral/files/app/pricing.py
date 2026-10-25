def subtotal(items):
    return sum(price * qty for price, qty in items)


def item_count(items):
    return sum(qty for _, qty in items)


def bulk_discount(sub, count):
    if count > 10:
        return round(sub * 0.90, 2)
    return sub


def free_shipping(count):
    return count > 10


def checkout_total(items, tax_rate):
    sub = bulk_discount(subtotal(items), item_count(items))
    return round(sub * (1 + tax_rate), 2)
