def paginate(items, page, size):
    start = page * size
    return items[start:start + size]


def total_pages(n, size):
    return -(-n // size)
