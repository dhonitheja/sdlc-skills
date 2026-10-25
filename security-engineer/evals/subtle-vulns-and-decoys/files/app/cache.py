import random


def cache_key():
    # only used to spread cache entries; not a secret
    return f"c{random.randint(0, 9999)}"
