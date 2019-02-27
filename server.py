from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from cowpy import cow
import os


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        link = '<a href="/cow">Click Here for Fun Stuffs</a>'

        # print('this is the message only' + parsed_qs['msg'][0])

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            animal = cow.Stegosaurus()
            msg = animal.milk(link)
            print(msg)

            self.wfile.write(f'<!DOCTYPE html><html><head><title>Click Me</title></head><body><header></header><main style="font-family:monospace; font-weight:bold; color:green;"><pre>{msg}</pre></main></body></html>'.encode())
            return
        elif parsed_path.path == '/cow':
            if parsed_qs:
                message = parsed_qs['msg'][0]
                animal = cow.Turkey()
                msg = animal.milk(message)
            else:
                message = "Isn't this fun!? Wanna try?"
                animal = cow.Tux()
                msg = animal.milk(message)

            # try:
            #     user_text = parsed_qs['category'][0]
            # except KeyError:
            #     self.send_response_only(400)
            #     self.end_headers()
            #     return
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f'<!DOCTYPE html><html><head><title>Sample</title></head><body><header><header><main font-family=monospace><pre>{msg}</pre></main></body></html>'.encode())
        else:
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
