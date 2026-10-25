from app import rates


def convert(amount, currency):
    return round(amount * rates.fetch_rate(currency), 2)
