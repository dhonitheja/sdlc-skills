import urllib.request


def fetch_preview(url):
    with urllib.request.urlopen(url, timeout=5) as r:
        return r.read(2048)
