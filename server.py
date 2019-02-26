from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from cowpy import cow
import os


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)
        print(parsed_qs)

        message = parsed_qs['msg'][0]

        print('this is the message only' + parsed_qs['msg'][0])

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            koala = cow.Moose()
            msg = koala.milk(message)
            print(msg)

            self.wfile.write(f'<!DOCTYPE html><html><head><title> cowsay </title></head><body><header><nav><ul><li><a href="/cow">Click Here for Fun Stuffs</a></li></ul></nav><header><main>{msg}</main></body></html>'.encode())
            return
        elif parsed_path.path == '/cow':
            try:
                user_text = parsed_qs['category'][0]
            except KeyError:
                self.send_response_only(400)
                self.end_headers()
                return
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f'<!DOCTYPE html><html><head><title> {user_text} </title></head><body><header><h1>Welcome to Cow Pie Central!</h1><header><main><h2>Instructions:</h2><p></p></main></body></html>'.encode())
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
