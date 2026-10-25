import json
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

import yaml

from config import PORT, INVENTORY_URL

SETTINGS = yaml.safe_load("currency: USD")


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        item = self.path.rsplit("/", 1)[-1]
        with urllib.request.urlopen(f"{INVENTORY_URL}/stock/{item}", timeout=5) as r:
            stock = json.load(r)["in_stock"]
        self.send_response(200 if stock > 0 else 409)
        self.end_headers()
        self.wfile.write(json.dumps({"item": item, "currency": SETTINGS["currency"]}).encode())


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
