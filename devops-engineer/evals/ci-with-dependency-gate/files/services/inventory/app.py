import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from config import PORT, STOCK


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        item = self.path.rsplit("/", 1)[-1]
        body = json.dumps({"item": item, "in_stock": STOCK.get(item, 0)}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
