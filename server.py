from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import os


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'<!DOCTYPE html><html><head><title> cowsay </title></head><body><header><nav><ul><li><a href="/cow">Click Here for Fun Stuffs</a></li></ul></nav><header><main>project description</main></body></html>'.encode())
            return
        elif parsed_path.path == '/test':
            try:
                cat = parsed_qs['category'][0]
                # print(parsed_qs['category'])
            except KeyError:
                self.send_response_only(400)
                self.end_headers()
                return
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f'<html><body><h1>{cat}</h1></body></html>'.encode())
            return
        elif parsed_path.path == '/cow':
            try:
                cowsay = parsed_qs['category'][0]
            except KeyError:
                self.send_response_only(400)
                self.end_headers()
                return
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f'<!DOCTYPE html><html><head><title> cowsay </title></head><body><header><nav><ul><li><a href="/cow">{cowsay}</a></li></ul></nav><header><main>project description</main></body></html>'.encode())
        self.send_response_only(404)
        self.end_headers()

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f'<!DOCTYPE html><html><head><title> cowsay </title></head><body><header><nav><ul><li><a href="/cow">cowsay</a></li></ul></nav><header><main>project description</main></body></html>'.encode())

if __name__ == "__main__":
    server_address = ('', 5000)
    server = HTTPServer(server_address, RequestHandler)
    server.serve_forever()
