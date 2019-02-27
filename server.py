from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from cowpy import cow
import requests
import json


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Method to create routes on '/' and '/cow' and create cow instances and drawings based on whether there is a query string and what the contents of that query string are.
        """
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        link = '<a href="/cow">Click Here for Fun Stuffs</a>'

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            animal = cow.Stegosaurus()
            msg = animal.milk(link)

            self.wfile.write(f'<!DOCTYPE html><html><head><title>Click Me</title></head><body><header></header><main style="font-family:monospace; font-weight:bold; color:green;"><pre>{msg}</pre></main></body></html>'.encode())
            return
        elif parsed_path.path == '/cow':
            if parsed_qs:
                try:
                    message = parsed_qs['msg'][0]
                    animal = cow.Turkey()
                    msg = animal.milk(message)
                except KeyError:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(f'<!DOCTYPE html><html><head><title>Sample</title></head><body><header><header><main font-family=monospace><pre>{msg}</pre></br></br><h2>Instructions:</h2><p>In the url, after "/cow" type "?msg=" and your message. Instead of spaces, use the "+" sign, and please avoid using special characters!</p></main></body></html>'.encode())
                    return
            else:
                message = "Isn't this fun!? Wanna try?"
                animal = cow.Tux()
                msg = animal.milk(message)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(f'<!DOCTYPE html><html><head><title>{message}</title></head><body><header><header><main font-family=monospace><pre>{msg}</pre></br></br><h2>Instructions:</h2><p>In the url, after "/cow" type "?msg=" and your message. Instead of spaces, use the "+" sign, and please avoid using special characters!</p></main></body></html>'.encode())
        else:
            self.send_response_only(404)
            self.end_headers()

    def do_POST(self):
        """
        Method to create POST route on any path that returns a JSON object with the client's query string as the value of key 'msg'.
        """
        content_length = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_length).decode()

        parsed_json = json.loads(post_body)
        message = parsed_json['msg']
        animal = cow.Squirrel()
        msg = animal.milk(message)

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()


def run_forever():
    """
    Method to start up the server.
    """
    port = 5000
    server_address = ('localhost', port)
    server = HTTPServer(server_address, RequestHandler)
    try:
        print(f'Starting server on PORT {port}')
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()

if __name__ == "__main__":
    run_forever()
