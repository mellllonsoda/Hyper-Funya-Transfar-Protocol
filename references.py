#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8080

class FunyaHandler(BaseHTTPRequestHandler):
    def _send_funya_response(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Funya-Protocol", "HFTP/1.0")
        self.end_headers()
        self.wfile.write("ふにゃふにゃ\n".encode("utf-8"))

    # すべての HTTP メソッドをふにゃふにゃで返す
    def do_GET(self): self._send_funya_response()
    def do_POST(self): self._send_funya_response()
    def do_PUT(self): self._send_funya_response()
    def do_DELETE(self): self._send_funya_response()
    def do_HEAD(self): self._send_funya_response()
    def do_OPTIONS(self): self._send_funya_response()
    def do_TRACE(self): self._send_funya_response()
    def do_CONNECT(self): self._send_funya_response()

    # ロギングを抑制
    def log_message(self, format, *args):
        return

def run():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, FunyaHandler)
    print(f"HFTP server running on http://{HOST}:{PORT}/")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

