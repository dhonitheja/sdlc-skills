from datetime import datetime


def is_open():
    now = datetime.now()
    return now.weekday() < 5 and 9 <= now.hour < 17


def greeting():
    return "We are open" if is_open() else "We are closed"
