import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("STUB_PORT", "8201"))
RATES = {"EUR": 2.0, "GBP": 1.5}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        cur = self.path.rsplit("/", 1)[-1].upper()
        if cur not in RATES:
            self.send_response(404)
            self.end_headers()
            return
        body = json.dumps({"data": {"currency": cur, "rate": RATES[cur]}}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
